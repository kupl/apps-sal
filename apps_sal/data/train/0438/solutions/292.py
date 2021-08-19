class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        parents = list(range(N))
        sizes = [0 for _ in range(N)]
        m_count = 0

        def find(i):
            if i != parents[i]:
                parents[i] = find(parents[i])
            return parents[i]

        def merge(i, j):
            nonlocal m_count
            parent_i = find(i)
            parent_j = find(j)
            if parent_i != parent_j:
                if sizes[parent_j] == m:
                    m_count -= 1
                if sizes[parent_i] == m:
                    m_count -= 1
                sizes[parent_j] += sizes[parent_i]
                if sizes[parent_j] == m:
                    m_count += 1
                parents[parent_i] = parent_j
        groups = [0] * N
        latest_round = -1
        for (i, a) in enumerate(arr, start=1):
            a -= 1
            groups[a] = 1
            sizes[a] = 1
            if m == 1:
                m_count += 1
            if a - 1 >= 0 and groups[a - 1] == 1:
                merge(a - 1, a)
            if a + 1 < N and groups[a + 1] == 1:
                merge(a, a + 1)
            if m_count > 0:
                latest_round = i
        return latest_round
