class Solution:
    def knightDialer(self, n: int) -> int:
        
        # pad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
        
        graph = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,9,3],5:[],6:[0,7,1],7:[2,6],8:[1,3],9:[4,2]}
        
        # self.dirs = [(1,2),(2,1),(-1,2),(-2,1),(-1,-2),(-2,-1),(2,-1),(1,-2)]
        
        ans = 0
        
        self.cache = {}
        
        for u in list(graph.keys()):
            
            ans += self.dial(graph,u,n-1)
        
        return ans % (10**9 + 7)
    
    def dial(self,graph,start,n):
        
        if n == 0:
            return 1
        
        ans = 0
        
        key = str(start) + ' ' + str(n)
        
        if key in list(self.cache.keys()):
            
            return self.cache[key]
        
        for v in graph[start]:
            ans += self.dial(graph,v,n-1)
            
        self.cache[key] = ans
            
        return self.cache[key]
                
            
            
        
        
        
        

