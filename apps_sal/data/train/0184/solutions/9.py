class Solution:
    def maxRepOpt1(self, text: str) -> int:
        inuse = collections.defaultdict(int)  # chars used in the repeated substring
        left = collections.defaultdict(int)  # not used chars
        MOVE_TO_THE_NEXT_CHAR = 1
        REPLACE = 0
        LEAVE_AS_IT_IS = -1
        res, i, n = 1, 0, 0

        # initially no chars are used yet
        for ch in text:
            left[ch] += 1

        for j, ch in enumerate(text):
            inuse[ch] += 1  # since we use this char
            left[ch] -= 1  # subtract its count from left dict
            n = max(inuse[ch], n)

            # this defines action we are going to take
            action = j - i - n

            char_exists = False
            if action >= MOVE_TO_THE_NEXT_CHAR:
                inuse[text[i]] -= 1
                left[text[i]] += 1  # add it to the left dict back, since it is no longer in use
                i += 1

            # we can replace only if we have unused char in the left dict
            elif action == REPLACE:
                char_exists = left[ch] > 0

            elif action == LEAVE_AS_IT_IS:
                char_exists = True

            if char_exists and j - i >= res:
                res = j - i + 1

        return res
