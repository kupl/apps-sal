class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for k in range(1, n):
            a, e, i, o, u = i + e + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)

        #***** BRute Force *****#
#         dic = {
#             'e' : {'a','i'},
#             'a' : {'i', 'e', 'u'},
#             'i' : {'e', 'o'},
#             'o' : {'i'},
#             'u' : {'i','o'},
#         }

#         def bfs(q, dic, ans):
#             while(q):
#                 vov, dist = q.popleft()
#                 #print(vov, dist)
#                 if(dist == n):
#                     ans = ans + 1
#                 if(dist > n):
#                     break
#                 for ch in dic[vov]:
#                     #print(ch,dist+1, \"*\")
#                     q.append((ch,dist+1))
#                     #visited.add(ch)
#             return ans


#         result = 0
#         for k in ['a', 'e', 'i', 'o', 'u']:
#             q = deque()
#             q.append((k, 1))
#             # visited = set()
#             # visited.add(k)
#             ans = bfs(q, dic, 0)
#             result = result + ans

#         return result
