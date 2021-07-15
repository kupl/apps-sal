
# we can memorize the path while doing dp
# let dp[used][i] = (string length, actual string) represents the bitmask used ends with ith element.

class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        common = {}
        for i, s1 in enumerate(A):
            for j in range(i):
                s2 = A[j]
                longest1, longest2 = 0, 0
                for k in range(min(len(s1), len(s2)) + 1):
                    if s1.endswith(s2[:k]):
                        longest1 = k
                    if s2.endswith(s1[: k]):
                        longest2 = k
                common[(i, j)] = longest1
                common[(j, i)] = longest2
        
        end = 1 << n
        dp = [[(float('inf'), '') 
               for i in range(n)] for m in range(end)]
        le, res = float('inf'), ''
        for used in range(end):
            for i, s in enumerate(A):
                if (used >> i) & 1 != 1:
                    continue
                mask = 1 << i
                if used ^ mask == 0:
                    dp[used][i] = (len(A[i]), A[i])
                else:
                    for j, last in enumerate(A):
                        if i == j or (used >> j) & 1 != 1:
                            continue
                        l, pref = dp[used ^ mask][j]
                        cand = pref + A[i][common[(j, i)] :]    
                        if len(cand) < dp[used][i][0]:
                            dp[used][i] = (len(cand), cand)
                if used == end - 1 and dp[used][i][0] < le:
                    le, res = dp[used][i]
        return res


# class Solution:
    
#     def addCost(self, from_word, to_word):
#         n = min(len(from_word), len(to_word))
#         cost = len(to_word)
#         for i in range(n):
#             if from_word[-i-1] == to_word[i]:
#                 cost -= 1
#         return cost 
    
#     def shortestSuperstring(self, A: List[str]) -> str:
#         # initalize 2D adjacency matrix
#         n = len(A)
#         adj_mat = [[0,] * n, ] * n
#         # travers words list, memo the cost by adj_mat
#         for i in range(n):
#             for j in range(n):
#                 if r != c:
#                     from_word, to_word = A[i], A[j]
#                     adj_mat[i][j] = self.addCost(from_word, to_word)
#         # DP memo, the length of start words as the initial values 
#         # dp = [len(w) for w in A] * n 
#         dp = [0, ] * n
#         for i, w in enumerate(A):
#             visited = {w}
#             dp[i] = len(w)
#             while len(visited) < n:
#                 from_w = w
#                 to_w = min(adj_mat[from_w])
                
        
        

