class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        memo = {}

        def helper(w, h):
            if w > h:
                w, h = h, w
            if (w, h) not in memo:
                if w == h:
                    ans = 1
                elif w == 1:
                    ans = h
                elif w == 0:
                    ans = 0
                else:
                    ans = w * h
                    for iw in range(1, w // 2 + 1):
                        ans = min(ans, helper(iw, h) + helper(w - iw, h))
                    for ih in range(1, h // 2 + 1):
                        ans = min(ans, helper(w, ih) + helper(w, h - ih))
                    for iw in range(1, (w + 1) // 2):
                        for ih in range(1, (h + 1) // 2):
                            for s in range(1, min(w - 2 * iw, h - 2 * ih) + 1):
                                ans = min(ans, 1 + helper(iw + s, ih) + helper(w - iw - s, ih + s) +
                                          helper(w - iw, h - ih - s) + helper(iw, h - ih))
                memo[(w, h)] = ans
            return memo[(w, h)]
        return helper(n, m)
