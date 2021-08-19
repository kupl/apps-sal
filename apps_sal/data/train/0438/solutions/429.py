class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:  # 最后一步才出现满足条件
            return m

        A = [i for i in range(n)]
        length = [0 for _ in range(n)]
        ans = -1

        def find(u):
            if u != A[u]:
                A[u] = find(A[u])
            return A[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False

            A[max(pu, pv)] = min(pu, pv)
            # 只修改新父节点的长度，节省时间。其他的用不到
            length[min(pu, pv)] += length[max(pu, pv)]

        for i, a in enumerate(arr):
            a -= 1
            length[a] = 1
            for j in [a - 1, a + 1]:
                # 查找两边是否是1，如果是1，则联合起来
                if 0 <= j < n:
                    # 如果j位置的长度是m，则记录上一步是满足条件的(最后一步无法记录)
                    if length[find(j)] == m:
                        ans = i
                    if length[j]:
                        union(j, a)
                        # print(length)

        # print(length)

        return ans
