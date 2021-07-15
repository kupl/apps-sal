class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        bfs=[]
        oinitial=set(initial)
        for i in initial:
            bfs.append([i,i])
        #print(bfs)
        frm={}
        
        
        for init in initial:
            seen=set(initial)
            bfs=[init]
            for n in bfs:
                for i,c in enumerate(graph[n]):
                    if i==n or i in seen or c==0:continue
                    seen.add(i)
                    if i in frm:
                        frm[i].append(init)
                    else:
                        frm[i]=[init]
                    bfs.append(i)
        
        #print(frm)
        #print(src)
        res=[0]*len(graph)
        
        for k in frm:
            if len(frm[k])==1:
                res[frm[k][0]]+=1
        
        
        if max(res)==0:return min(initial)
        
        return res.index(max(res))
                
            
            
            
        
        
        
            
                
                
            

