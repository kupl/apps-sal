class Solution:
    def minJumps(self, arr: List[int]) -> int:
        '''
        #最短就利用BFS
        '''
        n = len(arr)
        g = collections.defaultdict(list)
        for i, v in enumerate(arr):
            g[v].append(i)
        # 存放同值的位置
        visit = [0] * n
        values = set()
        step = 0
        q = [0]
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.pop(0)
                if cur == n - 1:
                    return step
                for i in [cur - 1, cur + 1]:
                    if 0 <= i < n and not visit[i]:
                        visit[i] = 1
                        q.append(i)
                if arr[cur] not in values:
                    values.add(arr[cur])
                    for i in g[arr[cur]]:
                        if not visit[i]:
                            visit[i] = 1
                            q.append(i)
            step += 1
        return step
