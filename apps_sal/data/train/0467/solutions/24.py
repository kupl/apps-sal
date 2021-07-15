class Solution:
    def sumFourDivisors(self, nums: List[int], c={}) -> int:
        r = 0
        for n in nums:
            if n in c:
                r += c[n]
                continue
            s = 0
            cnt = 0
            for i in range(1, round(sqrt(n) + 1)):
                if n % i == 0:
                    cnt += 1
                    if cnt > 4:
                        s = 0
                        break
                    s += i
                    j = n // i
                    if j != i:
                        cnt += 1
                        if cnt > 4:
                            s = 0
                            break
                        s += j
            if cnt == 4:
                c.update({n:s})
                r += s
            else:
                c.update({n:0})
        return r
