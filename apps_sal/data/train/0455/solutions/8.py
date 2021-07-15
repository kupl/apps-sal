class Solution:
    def isPrintable(self, A: List[List[int]]) -> bool:
        m, n = len(A), len(A[0])
        
        c = collections.Counter()
        dic = collections.defaultdict(lambda: [m+n, -1, m + n, -1, 0])
        seen = set()
        removed = set()
        for i, row in enumerate(A):
            for j, x in enumerate(row):
                dic[x][0] = min(dic[x][0], i)
                dic[x][2] = min(dic[x][2], j)
                dic[x][1] = max(dic[x][1], i)
                dic[x][3] = max(dic[x][3], j)
                dic[x][4] += 1
                seen.add(x)
        #print(dic)
        def helper(x):
            return abs((dic[x][1] - dic[x][0] + 1)*(dic[x][3] - dic[x][2] + 1) - dic[x][4])
        
        temp = sorted(seen, key = helper)
        
        #print(temp)
        
        k = 0
        #flag = True
        while len(temp) != len(removed):
            #flag= False 
            for t in temp:
                if t in removed: continue
                if helper(t) == 0:
                    removed.add(t)
                    break
                else:
                    a, b, c, d, total = dic[t]
                    flag = True
                    for i in  range(a, b + 1):
                        for j in range(c, d + 1):
                            if A[i][j]!= t and A[i][j] not in removed:
                                flag = False
                                break
                        if not flag:
                            break
                    #print(t, flag)
                    if flag:
                        removed.add(t)
                        break
            else:
                break
        return len(temp) == len(removed)
                        


