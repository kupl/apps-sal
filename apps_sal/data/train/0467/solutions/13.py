class Solution:
    def sumFourDivisors(self, nums: List[int], c={}) -> int:
        r = 0
        for n in nums:
            if n in c:
                r += c[n]
                continue
            s = n + 1
            cnt = 2
            e = sqrt(n)
            if (end := int(e)) == e:
                s += end
                cnt += 1
                end -= 1
            for i in range(2, end + 1):
                if n % i == 0:
                    cnt += 2
                    if cnt > 4:
                        s = 0
                        break
                    s += i
                    s += n // i
            if cnt == 4:
                c.update({n: s})
                r += s
            else:
                c.update({n: 0})
        return r
