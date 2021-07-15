##we need to find out for indices i which ones such that a[0],a[1],...,a[i] are permutations of 1,2,...,i+1.
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        minimum = len(light)+1
        maximum = 0
        moments = 0
        for index,num in enumerate(light):
            minimum = min(num,minimum)
            maximum = max(num,maximum)
            if minimum == 1 and maximum == index+1:
                moments += 1
        return moments

