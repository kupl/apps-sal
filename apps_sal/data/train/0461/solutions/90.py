class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
#         dic = collections.defaultdict(list)
#         for emp,mng in enumerate(manager):
#             dic[mng].append([emp,informTime[mng]])

#         bfs = [[headID,0]]
#         ans = {}
#         while(bfs):
#             for i in range(len(bfs)):
#                 cur_mng,time = bfs.pop(0)
#                 ans[cur_mng] = time
#                 bfs += [[x,y+time] for x,y in dic[cur_mng]]
#         return max(ans.values())

        g = collections.defaultdict(list)
        for i, v in enumerate(manager):
            g[v].append(i)
        
        def dfs(i):
            return informTime[i] if not g[i] else max([informTime[i] + dfs(c) for c in g[i]])
    
        return dfs(headID)
                
    
          #         0
          #        / \\
          #       1.  2
          #     / \\. / \\
          #    3  4. 5. 6
          #   /\\  /\\ /\\   /\\
          #  7  7 8 8 9 9 10 10
        
#         8
#         0
#         [-1,5,0,6,7,0,0,0]
#         [89,0,0,0,0,523,241,519]
        
#                         0
#                      / \\ \\ \\
#                     2   5 6 7
#                        / / /  
#                       1 3 4
                        
    
# 11
# 4
# [5,9,6,10,-1,8,9,1,9,3,4]
# [0,213,0,253,686,170,975,0,261,309,337]


#                          4         686
#                           \\
#                            10      337
#                            /
#                           3        253
#                          /
#                         9          309
#                        /|\\
#                       1 6 8        975
#                      /  |  \\
#                     7   2   5      170
#                              \\
#                               0    0

