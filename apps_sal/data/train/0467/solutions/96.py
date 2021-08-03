class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # go through the range of numbers in range(0, len(nums))
        # for each number go through the range(0, sqrt(num))
        # for the first loop initialize a set or an arrya to keep track that there are 4 divisors
        # go through the numbers, in the end if the len(set) == 4, get teh sum of array and append it to teh answer
        answer = 0
        for num in nums:
            mySet = set()
            for num2 in range(1, (int(sqrt(num)) + 1)):
                if (num % num2) == 0:
                    mySet.add(num2)
                    mySet.add(num / num2)
                    if len(mySet) > 4:
                        break
            print(mySet)
            if len(mySet) == 4:
                answer += int(sum(mySet))
        return answer
