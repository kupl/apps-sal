class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m

        groups = [(0, len(arr) + 1)]
        for i in range(len(arr) - 1, -1, -1):
            temp = []
            for start, end in groups:
                if start <= arr[i] < end:
                    if end - arr[i] - 1 == m or arr[i] - 1 - start == m:
                        return i
                    if end - 1 - arr[i] > m:
                        temp.append((arr[i], end))
                    if arr[i] - 1 - start > m:
                        temp.append((start, arr[i]))
                elif end - 1 - start >= m:
                    temp.append((start, end))
            groups = temp
        return -1
