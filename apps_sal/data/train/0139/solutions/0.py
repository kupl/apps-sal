class Solution:

    def minDeletionSize(self, A: List[str]) -> int:

        def isSorted(arr, i, j):
            return all((arr[k] <= arr[k + 1] for k in range(i, j)))
        ans = 0
        ranges = [[0, len(A) - 1]]
        for col in zip(*A):
            if not ranges:
                break
            if all((isSorted(col, i, j) for (i, j) in ranges)):
                tmp = []
                for (i, j) in ranges:
                    start = i
                    for k in range(i, j + 1):
                        if col[k] != col[start]:
                            if k - start > 1:
                                tmp.append([start, k - 1])
                            start = k
                    if j + 1 - start > 1:
                        tmp.append([start, j])
                    start = k
                ranges[:] = tmp
            else:
                ans += 1
        return ans
