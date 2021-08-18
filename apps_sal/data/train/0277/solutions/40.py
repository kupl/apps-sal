class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        b = 0
        ans = 0
        k = 0
        l = [0 for i in range(len(light))]
        for i in range(len(light)):
            a = light[i] - 1
            if b == a:
                l[a] = 2
                c = a + 1
                b = c
                while c < len(light) and l[c] == 1:
                    l[c] = 2
                    b = c + 1
                    k -= 1
                    c += 1
            else:
                if a > 0 and l[a - 1] == 2:
                    l[a] = 2
                    b = l[a] + 1
                else:
                    l[a] = 1
                    k += 1
            if k == 0:
                ans += 1
        return ans
