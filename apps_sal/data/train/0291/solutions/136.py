def isEven(n):
    return n % 2 == 0
def isOdd(n):
    return not isEven(n)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        od = list(range(len(arr)))
        ev = list(range(len(arr)))
        
        if isEven(arr[0]):
            od[0] = 0
            ev[0] = 1
        else:
            od[0] = 1
            ev[0] = 0

        for i, num in enumerate(arr):
            if i == 0:
                continue
            if isOdd(num):
                od[i] = ev[i-1] + 1
                ev[i] = od[i-1]
            else:
                od[i] = od[i-1]
                ev[i] = ev[i-1] + 1
        ans = 0
        
        for num in od:
            ans += num
        return ans % (10 ** 9 + 7)
