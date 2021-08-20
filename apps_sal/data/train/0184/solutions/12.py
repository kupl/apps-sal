class Solution:

    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        win = collections.Counter()

        def valid_win(win):
            if len(win) > 2:
                return False
            if len(win) == 1:
                return True
            return not all((n >= 2 for n in win.values()))
        max_c_idx = {}
        min_c_idx = {}
        for (i, c) in enumerate(text):
            if c not in max_c_idx:
                max_c_idx[c] = i
            elif i > max_c_idx[c]:
                max_c_idx[c] = i
            if c not in min_c_idx:
                min_c_idx[c] = i
        (left, right) = (0, 0)
        ans = 0
        while right < n:
            c = text[right]
            right += 1
            win[c] += 1
            while not valid_win(win) and left < right:
                d = text[left]
                left += 1
                win[d] -= 1
                if win[d] == 0:
                    win.pop(d)
            if len(win) == 1:
                ans = max(ans, right - left)
            else:
                (k1, k2) = win.keys()
                if win[k1] == 1 and (max_c_idx[k2] >= right or min_c_idx[k2] < left):
                    ans = max(ans, right - left)
                elif win[k2] == 1 and (max_c_idx[k1] >= right or min_c_idx[k1] < left):
                    ans = max(ans, right - left)
                else:
                    ans = max(ans, right - left - 1)
        return ans
