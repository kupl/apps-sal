class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        first = 0
        last = 1
        on = [False] * len(light)
        ans = 0
        for l in light:
            # print(on, first, l, last)
            on[l - 1] = True
            last = max(l, last)
            if first + 1 == l:
                while first < len(light) and on[first]:
                    first += 1
                if first == last:
                    ans += 1
        return ans
