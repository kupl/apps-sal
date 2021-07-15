class Solution:
    def maxRepOpt1(self, text: str) -> int:
        for k,g in itertools.groupby(text):
            print(g)
        G = [[k,len(list(g))] for k,g in itertools.groupby(text)]
        c = collections.Counter(text)
        
        res = max(min(n+1, c[k]) for k,n in G)
        
        for i in range(1,len(G)-1):
            if G[i-1][0] == G[i+1][0] and G[i][1] == 1:
                res = max(min(G[i-1][1]+G[i+1][1]+1, c[G[i-1][0]]), res)
        return res
