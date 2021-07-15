class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 0: 
            return 0
        result = 0
        num_odd = 0
        Cum = [0]
        for i in range(len(arr)):
            Cum.append(Cum[-1] + arr[i])
            if Cum[-1] % 2 != 0:
                num_odd += 1
        #print(num_odd)
        return (len(arr) + 1 - num_odd) * num_odd % (10**9+7)

