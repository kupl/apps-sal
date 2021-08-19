
# class Solution:
#     def knightDialer(self, n: int) -> int:
#         possible_moves = {1:[6,8], 2:[7,9], 3:[4,8], 4:[3,9,0], 5:[],
#                           6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2,4], 0:[4,6]}

#         self.memo = {}
#         def dfs(cur_point, count, n):
#             if count == n:
#                 return 1
#             if (cur_point, count) not in self.memo:
#                 self.memo[(cur_point, count)] = sum(dfs(nxt_point, count + 1, n) for nxt_point in possible_moves[cur_point])
#                 if cur_point in [1,4,7]:
#                     self.memo[(cur_point+2, count)] = self.memo[(cur_point, count)]
#                 elif cur_point in [3,6,9]:
#                     self.memo[(cur_point-2, count)] = self.memo[(cur_point, count)]
#             return self.memo[(cur_point, count)]


#         return sum(dfs(i, 1, n) for i in range(10)) % (10**9 + 7)

class Solution:
    d = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]       # Create a graph, index is the vertex and values are the edges
    cache = {}

    def dfs(self, i, n):
        if n == 0:
            return 1
        elif (i, n) not in self.cache:
            self.cache[i, n] = sum(self.dfs(val, n - 1) for val in self.d[i])  # Memoization
            if i in [1, 4, 7]:
                self.cache[i + 2, n] = self.cache[i, n]           # Symmetry
            elif i in [3, 6, 9]:
                self.cache[i - 2, n] = self.cache[i, n]
        return self.cache[i, n]

    def knightDialer(self, n: int) -> int:
        return sum(self.dfs(i, n - 1) for i in range(10)) % (int(1e9) + 7)
