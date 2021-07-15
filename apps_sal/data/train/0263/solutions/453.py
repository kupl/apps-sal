class Solution:
    def knightDialer(self, n: int) -> int:
        N = n
        transition = {1:[6,8],
        2:[7,9],
        3:[4,8],
        4:[3,9,0],
        5:[],
        6:[1,7,0],
        7:[2,6],
        8:[1,3],
        9:[2,4],
        0:[4,6]}
        # key:cur position
        # value: next position
        self.count = 0
        self.mem = {}
        
        def dfs(cur,steps):
            if steps==2:
                #self.count+=len(transition[cur])
                return len(transition[cur])
            else:
                tmp = 0
                if (cur,steps) in self.mem:
                    return self.mem[(cur,steps)]
                
                for neigh in transition[cur]:
                    tmp +=dfs(neigh,steps-1)
                    #print(tmp)
                self.mem[(cur,steps)] = tmp
                
                return self.mem[(cur,steps)]
        
        if N==1:
            return 10
        
        for i in range(10):
            self.count+=dfs(i,N)
        
        return self.count%(10**9+7)
    
#         if n==1:
#             return 10
        
#         jump = {0:[4,6],
#                 1:[6,8],
#                2:[7,9],
#                3:[4,8],
#                4:[3,9,0],
#                5:[],
#                6:[1,7,0],
#                7:[2,6],
#                8:[1,3],
#                9:[2,4]}
        
#         def get(n,d):
#             if n==1:
#                 s = 0
#                 for key in d.keys():
#                     s+=d[key]
                    
#                 return s%(10**9+7)
#             new_d = collections.defaultdict(int)
#             for key in d.keys():
#                 nexts = jump[key]
#                 for next in nexts:
#                     new_d[next]+=d[key]
            
#             return get(n-1,new_d)
#         count = 0
#         for i in range(10):
#             d = collections.defaultdict(int)
#             d[i]=1
#             count+=get(n,d)
            
#         return count%(10**9+7)

