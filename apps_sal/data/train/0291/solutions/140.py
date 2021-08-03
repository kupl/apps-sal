class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
        odd[i] = number of sub arrays with odd sum and end at i
        even[i] = number of sub arrays with even sum and end at i
        '''
        odd = [0 for x in arr]
        even = [0 for x in arr]
        odd[0] = 1 if arr[0] % 2 == 1 else 0
        even[0] = 1 if arr[0] % 2 == 0 else 0
        for i in range(1, len(arr)):
            if arr[i] % 2 == 0:
                odd[i] = odd[i - 1]
                even[i] = even[i - 1] + 1
            else:
                odd[i] = even[i - 1] + 1
                even[i] = odd[i - 1]
        return sum(odd) % 1000000007
