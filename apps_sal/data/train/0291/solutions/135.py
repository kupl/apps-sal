class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        count = len(arr)
        isodd = [item % 2 for item in arr]
        odd_end_total = [0] * count
        even_end_total = [0] * count
        odd_end_total[0] = isodd[0]
        even_end_total[0] = 1 - odd_end_total[0]
        for index in range(1, count):
            if isodd[index]:
                odd_end_total[index] = 1 + even_end_total[index - 1]
                even_end_total[index] = odd_end_total[index - 1]
            else:
                odd_end_total[index] = odd_end_total[index - 1]
                even_end_total[index] = 1 + even_end_total[index - 1]
        result = 0
        for index in range(count):
            result += odd_end_total[index]
        return result % 1000000007
