class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def get_divs(num):
            divs = []
            for i in range(1, int(sqrt(num)) + 1):
                if not num % i:
                    divs.append(i)
                    if i != int(num / i):
                        divs.append(int(num / i))
                if len(divs) > 4:
                    return None
            if len(divs) < 4:
                return None
            return sum(divs)
        ans = 0
        for item in nums:
            divs = get_divs(item)
            if divs:
                ans += divs
        return ans
