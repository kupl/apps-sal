class Solution:

    def maxRepOpt1(self, text: str) -> int:
        inuse = collections.defaultdict(int)
        left = collections.defaultdict(int)
        MOVE_TO_THE_NEXT_CHAR = 1
        REPLACE = 0
        LEAVE_AS_IT_IS = -1
        (res, i, n) = (1, 0, 0)
        for ch in text:
            left[ch] += 1
        for (j, ch) in enumerate(text):
            inuse[ch] += 1
            left[ch] -= 1
            n = max(inuse[ch], n)
            action = j - i - n
            char_exists = False
            if action >= MOVE_TO_THE_NEXT_CHAR:
                inuse[text[i]] -= 1
                left[text[i]] += 1
                i += 1
            elif action == REPLACE:
                char_exists = left[ch] > 0
            elif action == LEAVE_AS_IT_IS:
                char_exists = True
            if char_exists and j - i >= res:
                res = j - i + 1
        return res
