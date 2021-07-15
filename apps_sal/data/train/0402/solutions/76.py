class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(i) for i in blocked}
        def bfs(source,target):
            que = [source]
            seen = {tuple(source)}
            for x,y in que:
                for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                    m,n = x+i,y+j
                    if 0<=m<10**6 and 0<=n<10**6 and (m,n) not in seen and (m,n) not in blocked:
                        if m == target[0] and n==target[1]:
                            return True
                        que.append((m,n))
                        seen.add((m,n))
                    if len(que)>=20000:
                        return True
            return False
        return bfs(source,target) and bfs(target,source)

