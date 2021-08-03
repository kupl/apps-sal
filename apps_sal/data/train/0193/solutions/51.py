class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        A = {}
        for x in arr:
            A[x] = A.get(x, 0) + 1

        p = 0
        count = 0
        for x in sorted(list(A.items()), key=lambda x: -x[1]):
            p += x[1]
            count += 1
            if p >= len(arr) // 2:
                return count
