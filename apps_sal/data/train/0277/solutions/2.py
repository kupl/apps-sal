class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        def natural_sum(n):
            return (n*(n+1))//2
        count, s = 0, 0
        for i in range(len(light)):
            s += light[i]
            if natural_sum(i+1) == s:
                count += 1
        return count
