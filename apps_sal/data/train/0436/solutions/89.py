class Solution:
    def minDays(self, n: int) -> int:
        queue = deque([n])
        visited = set()
        steps = 1

        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                remain = queue.popleft()
                if remain == 0:
                    return steps - 1
                if remain - 1 not in visited:
                    queue.append((remain - 1))
                    visited.add(remain - 1)
                if remain // 2 > 0 and remain % 2 == 0 and remain // 2 not in visited:
                    queue.append(remain // 2)
                    visited.add(remain // 2)
                if remain // 3 > 0 and remain % 3 == 0 and remain // 3 not in visited:
                    queue.append(remain // 3)
                    visited.add(remain // 3)
            steps += 1
        return steps


#         queue = deque([(n, 1)])
#         steps = 1

#         while queue:
#             q_len = len(queue)
#             for _ in range(q_len):
#                 remain, curr = queue.popleft()
#                 remain -= curr
#                 if remain == 0:
#                     print('hehe')
#                     return steps
#                 queue.append((remain, 1))
#                 if remain // 2 > 0 and remain % 2 == 0:
#                     queue.append((remain, remain // 2))
#                 if remain - 2 * remain // 3 > 0 and remain % 3 == 0:
#                     queue.append((remain, remain - 2 * remain // 3))
#             steps += 1
#         return steps
