class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        L = [None for i in range(N)]
        num_m_groups = 0
        latest_step = -1
        for i in range(N):
            idx = arr[i] - 1
            if (idx == 0 or L[idx - 1] == None) and (idx == N - 1 or L[idx + 1] == None):
                L[idx] = (idx, idx)
                diff = 1
                if m == diff:
                    num_m_groups += 1
            elif idx == 0 or L[idx - 1] == None:
                (x, y) = L[idx + 1]
                if y - x + 1 == m:
                    num_m_groups -= 1
                new_pair = (idx, y)
                L[idx] = new_pair
                L[y] = new_pair
                if y - idx + 1 == m:
                    num_m_groups += 1
            elif idx == N - 1 or L[idx + 1] == None:
                (x, y) = L[idx - 1]
                if y - x + 1 == m:
                    num_m_groups -= 1
                new_pair = (x, idx)
                L[idx] = new_pair
                L[x] = new_pair
                if idx - x + 1 == m:
                    num_m_groups += 1
            else:
                (x1, y1) = L[idx - 1]
                (x2, y2) = L[idx + 1]
                if y1 - x1 + 1 == m:
                    num_m_groups -= 1
                if y2 - x2 + 1 == m:
                    num_m_groups -= 1
                new_pair = (x1, y2)
                if y2 - x1 + 1 == m:
                    num_m_groups += 1
                L[x1] = new_pair
                L[y2] = new_pair
            if num_m_groups > 0:
                latest_step = i + 1
        return latest_step
