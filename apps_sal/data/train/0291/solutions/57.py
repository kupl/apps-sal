class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = [0]
        even = [0]
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                even.append(even[-1] + 1)
                odd.append(odd[-1])
            else:
                even.append(odd[-1])
                odd.append(even[-2] + 1)

        return sum(odd) % (10**9 + 7)
