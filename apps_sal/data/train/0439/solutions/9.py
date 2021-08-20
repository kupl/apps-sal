class Solution:

    def maxTurbulenceSize(self, array: List[int]) -> int:
        even = [1] * len(array)
        odd = [1] * len(array)
        for i in range(len(array) - 2, -1, -1):
            if array[i] > array[i + 1]:
                odd[i] += even[i + 1]
            if array[i] < array[i + 1]:
                even[i] += odd[i + 1]
        return max(max(even), max(odd))
