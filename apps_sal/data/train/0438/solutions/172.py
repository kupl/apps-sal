class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        a = [(1, len(arr))]
        if m == len(arr):
            return len(arr)

        def binSearch(ar, num) -> int:
            if len(ar) == 1:
                if ar[0][0] <= num <= ar[0][1]:
                    return 0
            (lo, hi) = (0, len(ar) - 1)
            while lo <= hi:
                mid = (lo + hi) // 2
                if ar[mid][1] < num:
                    lo = mid + 1
                elif num < ar[mid][0]:
                    hi = mid
                elif ar[mid][0] <= num <= ar[mid][1]:
                    return mid
                else:
                    return -1
            return -1
        for (i, n) in enumerate(arr[::-1]):
            idx = binSearch(a, n)
            el = a[idx]
            if el[0] == n:
                if el[1] == n:
                    del a[idx]
                else:
                    a[idx] = (n + 1, el[1])
            elif el[1] == n:
                if el[0] == n:
                    del a[idx]
                else:
                    a[idx] = (el[0], n - 1)
            else:
                a[idx] = (el[0], n - 1)
                a.insert(idx + 1, (n + 1, el[1]))
            if n - el[0] == m or el[1] - n == m:
                return len(arr) - i - 1
        return -1
