class Solution:
     def integerReplacement(self, n):
         """
         :type n: int
         :rtype: int
         """
         queue = collections.deque([n])
         step = 0
         while len(queue):
             sz = len(queue)
             while sz > 0:
                 sz -= 1
                 num = queue.popleft()
                 if num == 1:
                     return step
                 if num & 1:
                     queue.append(num + 1)
                     queue.append(num - 1)
                 else:
                     queue.append(num // 2)
             step += 1
         return step

