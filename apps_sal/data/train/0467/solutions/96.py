class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            mySet = set()
            for num2 in range(1, int(sqrt(num)) + 1):
                if num % num2 == 0:
                    mySet.add(num2)
                    mySet.add(num / num2)
                    if len(mySet) > 4:
                        break
            print(mySet)
            if len(mySet) == 4:
                answer += int(sum(mySet))
        return answer
