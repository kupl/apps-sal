class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        preference_list = [[0 for _ in range(n)] for _ in range(n)]
        
        for x in range(n):
            for i, y in enumerate(preferences[x]):
                preference_list[x][y] = n-i-1
            
        #print(preference_list)
        unhappy={}
        for i in range(n//2):
            x,y = pairs[i]
            for j in range(n//2):
                u,v = pairs[j]
                if i!=j:
                    if ((preference_list[x][y]<preference_list[x][u] and preference_list[u][x]>preference_list[u][v]) or (preference_list[x][y]<preference_list[x][v] and preference_list[v][u]<preference_list[v][x])):
                        #print(f'X-> x, y : {x, y}; u,v: {u,v}')
                        unhappy[x]=1
                    if ((preference_list[y][x]<preference_list[y][u] and preference_list[u][y]>preference_list[u][v]) or (preference_list[y][x]<preference_list[y][v] and preference_list[v][u]<preference_list[v][y])):
                        #print(f'Y->  y,x : {y,x}; u,v: {u,v}')
                        unhappy[y]=1
        #print(unhappy)
        res = len(unhappy)
            
        return res
