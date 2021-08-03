class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def get_divs(num):

            # print(num)
            divs = []
            for i in range(1, int(sqrt(num)) + 1):
                # print(divs)

                if(not num % i):
                    # divides
                    divs.append(i)
                    if(i != int(num / i)):
                        divs.append(int(num / i))

                if(len(divs) > 4):
                    return None

            # print(divs)
            if(len(divs) < 4):
                return None

            # print(divs)
            return sum(divs)

        ans = 0

        for item in nums:
            divs = get_divs(item)
            #print(item, divs)
            if(divs):
                ans += divs

        return ans
