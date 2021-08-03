class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        index = [-1 for i in range(len(arr))]
        groups = [0 for i in range(len(arr))]
        count, lastindex = 0, -1
        for i, num in enumerate(arr):
            a = num - 1
            groups[a], index[a], length = 1, a, 1
            if a - 1 >= 0 and groups[a - 1] == 1:
                left = index[a - 1]  # left index
                if a - left == m:
                    count -= 1
                index[left], index[a] = a, left  # left end
                length += (a - left)
            if a + 1 < len(arr) and groups[a + 1] == 1:
                left, right = index[a], index[a + 1]
                if right - a == m:
                    count -= 1
                index[right], index[left] = left, right
                length += (right - a)
            if length == m:
                count += 1
            if count > 0:
                lastindex = i + 1
        return lastindex
