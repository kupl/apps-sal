class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        m_cnt = 0
        parent = [i for i in range(N)]
        cnt = [1] * N
        mark = [0] * N

        def find(i):
            if parent[i] == i:
                return i
            else:
                parent[i] = find(parent[i])
                return parent[i]

        def union(i, j, m_cnt):
            x = find(i)
            y = find(j)
            if cnt[x] == m:
                m_cnt -= 1
            if cnt[y] == m:
                m_cnt -= 1
            if cnt[x] + cnt[y] == m:
                m_cnt += 1
            if x < y:
                parent[y] = x
                cnt[x] += cnt[y]
            else:
                parent[x] = y
                cnt[y] += cnt[x]

            return m_cnt

        ans = -1

        for i, x in enumerate(arr):
            mark[x - 1] = 1
            l = False
            r = False

            if m == 1:
                m_cnt += 1

            if x > 1 and mark[x - 2] == 1:
                m_cnt = union(x - 1, x - 2, m_cnt)
            else:
                l = True
            if x < N and mark[x] == 1:
                m_cnt = union(x - 1, x, m_cnt)
            else:
                r = True

            if m_cnt > 0:
                ans = i + 1

            # print(m_cnt)
        return ans
