class Solution:
    # Make prefix sum, store only whether sum is odd or even
    # Iterate through prefix sum, check if current prefix sum is odd/even and count number of odd/even subarrays behind it
    def numOfSubarrays(self, arr: List[int]) -> int:
        countOdd, countEven, result = 0, 1, 0
        modulo = 1000000007
        prev = 0
        for i in arr:
            prev = (prev + i) % 2
            if prev == 0:
                countEven += 1
                result += countOdd
                if result >= modulo:
                    result %= modulo
            else:
                countOdd += 1
                result += countEven
                if result >= modulo:
                    result %= modulo
        return result
