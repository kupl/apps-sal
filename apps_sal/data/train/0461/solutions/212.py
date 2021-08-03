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
            # if informTime[ii]==0: ## no sub
            #    continue
            if manager[ii] == -1:  # head
                time = informTime[ii]
                continue
            if manager[ii] not in ht:
                ht[manager[ii]] = {}
                ht[manager[ii]]['subord'] = []
                ht[manager[ii]]['time'] = informTime[ii]
            ht[manager[ii]]['subord'].append(ii)
        print(ht)

        queue = collections.deque()  # store managers only
        queue.append(headID)
        # print(queue)
        informed = 1
        while len(queue):
            n_sub = len(queue)
            # print('#########')
            # print(n_sub)
            for ii in range(n_sub):
                m = queue.popleft()
                # print('---------')
                # print(m)

                # print(ht[m])
                # if ii == 0:
                #    time += ht[m]['time'] ##same time/parallel
                if m in ht:
                    for e in ht[m]['subord']:
                        if e in ht:  # also a manager
                            queue.append(e)
                #print('after updating queue')
                # print(queue)
                #informed += 1
        return time
