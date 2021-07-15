class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(i,s):
            if i in visit or (i in ht and i!=s):
                return
            visit.add(i)
            source[i].append(s)
            for j in graph[i]:
                dfs(j,s)
     
        ht=set(initial)
        for i in range(len(graph)):
            tmp=[]  
            for j in range(len(graph[i])):
                if graph[i][j]:
                    tmp.append(j)
            graph[i]=tmp
                
        source=[[] for _ in range(len(graph))]
        for i in initial:
            visit=set()
            dfs(i,i)

        dic=collections.Counter()
        for i in range(len(source)):
            if len(source[i])==1:
                dic[source[i].pop()]+=1
        res,val=len(graph),0
        for i,cnt in list(dic.items()):
            if cnt>val:
                res,val=i,cnt
            elif cnt==val:
                res=min(res,i)

        return res
                
                
        

