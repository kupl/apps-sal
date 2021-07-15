class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ansIfOne = kadane(A)
        
        ansIfTwo = sum(A) - kadaneMin(A[1:len(A)-1])
        
        return max(ansIfOne, ansIfTwo)
        
        
        
def kadane(A):
    prevMax = -math.inf
    result = -math.inf
    for x in A:
        curMax = max(prevMax + x, x)
        prevMax = curMax
        result = max(result, curMax)
    return result

def kadaneMin(A):
    prevMin = math.inf
    result = math.inf
    for x in A:
        curMin = min(prevMin + x, x)
        prevMin = curMin
        result = min(result, curMin)
    return result

