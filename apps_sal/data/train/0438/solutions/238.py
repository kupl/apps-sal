class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        parent = [i for i in range(n)]
        cnt = [0]*n
        self.m_cnt = 0
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            old = (cnt[find(n1)] == m) + (cnt[find(n2)] == m)
            cnt[find(n2)] += cnt[find(n1)]
            parent[find(n1)] = find(n2)
            new = (cnt[find(n2)] == m)
            self.m_cnt += new-old
            
        string = [0]*n
        ans = -1
        for i in range(n):
            j = arr[i]-1
            string[j] = 1
            cnt[j] = 1
            if m == 1:
                self.m_cnt += 1
            if j>0 and string[j-1] == 1:
                union(j-1, j)
            if j<n-1 and string[j+1] == 1:
                union(j, j+1)
            if self.m_cnt > 0:
                ans = i+1
        return ans
        

