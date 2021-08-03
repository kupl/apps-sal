from math import sqrt, floor


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        def find(i, parent):
            if parent[i] == i:
                return i
            return find(parent[i], parent)

        def union(i, j, parent, cnt):
            p = find(i, parent)
            q = find(j, parent)
            if p == q:
                return

            if cnt[p] < cnt[q]:
                p, q = q, p

            cnt[p] += cnt[q]
            parent[q] = p

        m = max(A)
        arr = [True] * (m + 1)
        cnt = [1] * len(A)
        parent = [*list(range(len(A)))]

        for i in range(2, floor(sqrt(m)) + 1):
            if arr[i]:
                k = -1
                for j in range(len(A)):
                    if A[j] % i == 0:
                        while A[j] % i == 0:
                            A[j] = floor(A[j] / i)
                        if k == -1:
                            k = j
                        else:
                            union(k, j, parent, cnt)
                for j in range(i * i, m + 1, i):
                    arr[j] = False
        A = sorted([(x, i) for i, x in enumerate(A) if x > 1])
        for i in range(1, len(A)):
            if A[i - 1][0] == A[i][0]:
                union(A[i - 1][1], A[i][1], parent, cnt)

        return max(cnt)
