#math
#time:O(sqr(N))
'''
x + (x+1) + (x+2)+...+ k terms = N
kx + k*(k-1)/2 = N ->
kx = N - k*(k-1)/2 ->
N-k*(k-1)/2>0
'''
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        k,count = 1,0
        while N > k*(k-1)/2:
            if (N - k*(k-1)/2)%k == 0:
                count += 1
            k += 1
        return count
