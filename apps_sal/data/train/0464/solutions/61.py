class Solution:
    def minOperations(self, n: int) -> int:
        sum=0
        for i in range(n):
            sum +=2*i+1
        eq=sum/n

        step=0
        for i in range(int(n/2)):
            step +=int(eq-(2*i+1))
        return step
