class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        lim = len(arr)
        d = dict()
        
        for i in range(0,lim):
            if arr[i] in d:
                d[arr[i]].append(i)
            else:
                d[arr[i]]=[i]
        for x in d:
            d[x].sort(reverse=True)
        
        start = []
        a=[-1 for i in range(0,lim)]       
        start = [[0,0]]
        
        for x in d[arr[0]]:
            if x!=0:
                start.append([x,1])
                a[x]=1
        
        start.sort(key=lambda x: x[1])
        while 1!=-1:
            tmp = []
            
            for x in start:
                
                if x[0]==lim-1:
                    return x[1]
                if x[0]+1==lim-1:
                    return x[1]+1
                a[x[0]]=1
                if x[0]>0 and a[x[0]-1]==-1:
                    tmp.append([x[0]-1,x[1]+1])
                if a[x[0]+1]==-1:
                    tmp.append([x[0]+1,x[1]+1])
                for y in d[arr[x[0]]]:
                    
                    if a[y]==-1:
                        
                        tmp.append([y,x[1]+1])
              
            start = tmp
        
                
                

