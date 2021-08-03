class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:

        def factorize(num):
            power = 0
            while num % 2 == 0:
                num, power = num // 2, power + 1
            return (num, power)

        counts = defaultdict(lambda: [0] * 17)
        zeros = 0
        for a in A:
            if a == 0:
                zeros += 1
            else:
                n, p = factorize(a)
                counts[n][p] += 1

        if zeros % 2 == 1:
            return False

        for key in counts:
            carry = 0
            for p in counts[key]:
                carry = p - carry
                if carry < 0:
                    return False
            if carry != 0:
                return False

        return True
