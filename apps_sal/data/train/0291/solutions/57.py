class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # keep array that holds # of even/odd sum subarrays that end at that index
        odd = [0]
        even = [0]
        for i in range(len(arr)):
            if arr[i] % 2 == 0:  # even
                even.append(even[-1] + 1)
                odd.append(odd[-1])
            else:               # odd
                even.append(odd[-1])
                odd.append(even[-2] + 1)

        # print(\"EVEN:\",even)
        # print(\"ODD: \", odd)

        return sum(odd) % (10**9 + 7)
