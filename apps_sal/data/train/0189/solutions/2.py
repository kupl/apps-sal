class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = {}
        for i in range(len(preferences)):
            pref[i] = {}
            plist = preferences[i]
            for j in range(len(plist)):
                pref[i][plist[j]] = j
        print(pref)
            
        unhappy = set()
        for i in range(len(pairs)):
            for j in range(len(pairs)):                
                if i == j:
                    continue
                for x in pairs[i]:
                    y = pairs[i][1] if x == pairs[i][0] else pairs[i][0]
                    for u in pairs[j]:
                        v = pairs[j][1] if u == pairs[j][0] else pairs[j][0]
                        if (pref[x][y] > pref[x][u] and pref[u][v] > pref[u][x]):
                            unhappy.add(x)



        return len(unhappy)
