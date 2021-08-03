class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return len(arr)

        visited = set([0, len(arr) + 1])
        for i in range(len(arr) - 1, -1, -1):
            index = arr[i]
            if index + m + 1 in visited:
                for n in range(index, index + m + 1):
                    if n in visited:
                        break
                else:
                    return i

            if index - m - 1 in visited:
                for n in range(index - 1, index - m - 1, -1):
                    if n in visited:
                        break
                else:
                    return i
            visited.add(index)

        return -1
