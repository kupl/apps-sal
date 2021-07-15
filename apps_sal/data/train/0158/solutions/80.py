class Solution:
    def kSimilarity(self, A, B):
#         def nei(x):
#             i = 0
#             while x[i] == B[i]: i += 1
#             for j in range(i + 1, len(A)):
#                 if x[j] == B[j]:
#                     continue
#                 if x[j] == B[i] and x[i] == B[j]:
#                     yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]
#                     break
#                 if x[j] == B[i]:
#                     yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]



#         # def test():
#         stack = [(A, 0)]
#         visit = {A}
#         while stack:
#             cur, d = stack.pop()
#             if cur == B: return d
#             for neighbor in nei(cur):
#                 if neighbor not in visit:
#                     visit.add(neighbor)
#                     stack.append((neighbor, d+1))
                    
        
        n = len(A)
        def nei(x):
            i = 0
            while x[i] == B[i]: i += 1
            for j in range(i+1,n):
                if x[j] == B[j]:
                    continue
                if x[j] == B[i] and x[i] == B[j]:
                    yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
                    break
                if x[j] == B[i]:
                    yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
        pool = [(A,0)]
        seen = {A}
        for x,d in pool:
            if x == B: return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y)
                    pool.append((y,d+1))
