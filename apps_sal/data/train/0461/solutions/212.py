class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        cache = [-1] * n

        def dfs(cur):
            if cur == -1:
                return 0
            if cache[cur] == -1:
                cache[cur] = dfs(manager[cur]) + informTime[cur]
            return cache[cur]
        return max([dfs(i) for i in range(n)])

    def numOfMinutes_5pct(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        for ii in range(len(manager)):
            if informTime[ii] == 0:
                temp = 0
                index = ii
                while index != -1:
                    temp += informTime[index]
                    index = manager[index]
                res = max(res, temp)
        return res

    def numOfMinutes_dfs_wrong(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time = 0
        ht = {}
        for ii in range(len(manager)):
            if manager[ii] == -1:
                time = informTime[ii]
                continue
            if manager[ii] not in ht:
                ht[manager[ii]] = {}
                ht[manager[ii]]['subord'] = []
                ht[manager[ii]]['time'] = informTime[ii]
            ht[manager[ii]]['subord'].append(ii)
        print(ht)

        queue = collections.deque()
        queue.append(headID)
        informed = 1
        while len(queue):
            n_sub = len(queue)
            for ii in range(n_sub):
                m = queue.popleft()

                if m in ht:
                    for e in ht[m]['subord']:
                        if e in ht:
                            queue.append(e)
        return time
