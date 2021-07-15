# class Solution:
#     def minDays(self, n: int) -> int:
#         return self._find(n, {0: 0})
    
    
#     def _find(self, n, cache):

#         if n in cache:
#             return cache[n]
        
#         ret = inf
#         if n % 3 == 0:
#             ret = 1 + self._find(n // 3, cache)
#         if n % 2 == 0:
#             ret = min(ret, 1 + self._find(n // 2, cache))
#         if n < 50000:
#             ret = min(ret, 1 + self._find(n - 1, cache, terminate - 1))
        

#         return ret


# from collections import deque

# class Solution:
#     def minDays(self, n: int) -> int:
#         q1 = deque([0, None])
#         q2 = deque([n, None])
#         visited = {n}
        
#         for i in range(n):
#             tmp = set()
#             while True:
#                 n = q1.popleft()
#                 if n is None:
#                     q1.append(None)
#                     break
#                 for m in [n + 1, n * 2, n * 3]:
#                     if m in visited:
#                         return i * 2 + 1
#                     if m not in tmp:
#                         tmp.add(m)
#                         q1.append(m)
#             visited = tmp
            
#             tmp = set()
#             while True:
#                 n = q2.popleft()
#                 if n is None:
#                     q2.append(None)
#                     break
#                 l = [n - 1]
#                 if n % 2 == 0:
#                     l.append(n // 2)
#                 if n % 3 == 0:
#                     l.append(n // 3)
#                 for m in l:
#                     if m in visited:
#                         return i * 2 + 2
#                     if m not in tmp:
#                         q2.append(m)
#                         tmp.add(m)
#             visited = tmp


class Solution:
    def minDays(self, n: int) -> int:
        q1 = deque([0, None])
        q2 = deque([n, None])
        visited1 = {0}
        visited2 = {n}
        
        for i in range(n):
            while True:
                n = q1.popleft()
                if n is None:
                    q1.append(None)
                    break
                for m in [n + 1, n * 2, n * 3]:
                    if m in visited2:
                        return i * 2 + 1
                    if m not in visited1:
                        visited1.add(m)
                        q1.append(m)
            
            while True:
                n = q2.popleft()
                if n is None:
                    q2.append(None)
                    break
                l = [n - 1]
                if n % 2 == 0:
                    l.append(n // 2)
                if n % 3 == 0:
                    l.append(n // 3)
                for m in l:
                    if m in visited1:
                        return i * 2 + 2
                    if m not in visited2:
                        q2.append(m)
                        visited2.add(m)


# class Solution:
#     def minDays(self, n: int) -> int:
#         # self.hit0 = 0
#         # self.hit1 = 0
#         # self.total = 0
        
#         # cache = {0: 0}
#         # return self._find(n, cache, inf)
        
#         return self._find(n, {0: 0}, inf)
        
#         # self._find(n, cache, inf)
#         # hit = self.hit0 + self.hit1
#         # print(self.total, hit, self.hit0, self.hit1, hit / self.total, self.hit0 / hit)
        
#         # print(cache)
#         # return cache[n]


#     def _find(self, n, cache, terminate):
        
#         if n in cache:
#             return cache[n]
        
#         # # self.total += 1
#         # if n in cache:
#         #     if cache[n] > terminate:
#         #         # self.hit0 += 1
#         #         return inf
#         #     # self.hit1 += 1
#         #     return cache[n]
        
#         if terminate <= 0:
#             return inf
        
#         oldTerminate = terminate
#         ret = inf
#         if n % 3 == 0:
#             ret = 1 + self._find(n // 3, cache, terminate - 1)
#             terminate = min(terminate, ret - 1)
#         if n % 2 == 0:
#             ret = min(ret, 1 + self._find(n // 2, cache, terminate - 1))
#             terminate = min(terminate, ret - 1)
#         ret = min(ret, 1 + self._find(n - 1, cache, terminate - 1))
        
#         # if ret < inf:
#         #     cache[n] = ret
#         # return ret
        
#         if ret <= oldTerminate:
#             cache[n] = ret
#             return ret
#         return inf


# class Solution:
#     def minDays(self, n: int) -> int:
#         return self._find(n, {0: 0}, inf)
    
    
#     def _find(self, n, cache, terminate):

#         if n in cache:
#             return cache[n]
        
#         if terminate <= -15:
#             return inf
        
#         ret = inf
#         if n % 3 == 0:
#             ret = 1 + self._find(n // 3, cache, terminate - 1)
#             terminate = min(terminate, ret - 1)
#         if n % 2 == 0:
#             ret = min(ret, 1 + self._find(n // 2, cache, terminate - 1))
#             terminate = min(terminate, ret - 1)
#         ret = min(ret, 1 + self._find(n - 1, cache, terminate - 1))
        
#         if ret < inf:
#             cache[n] = ret
#         return ret


# class Solution:
#     def minDays(self, n: int) -> int:
#         arr = [0]
#         for i in range(1, n + 1):
#             n = arr[-1]
#             if i % 2 == 0:
#                 n = min(n, arr[i // 2])
#             if i % 3 == 0:
#                 n = min(n, arr[i // 3])
#             arr.append(n + 1)
        
#         return arr[-1]

