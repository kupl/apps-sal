class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = 0
        even = 0
        n = len(arr)
        sumlist = [0] * n
        output = 0
        for i in range(n - 1, -1, -1):
            if i != n - 1:
                sumlist[i] += arr[i] + sumlist[i + 1]
            else:
                sumlist[i] += arr[i]
            if sumlist[i] % 2 == 0:
                output += odd
                even += 1
            else:
                output += 1
                output += even
                odd += 1
            output %= 10 ** 9 + 7
        return output
