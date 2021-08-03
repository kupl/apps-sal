class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        # Array of Doubled Pairs 9/24 8/31/20
        # 1:43 9/1/2020
        #         c = collections.Counter(A)
        #         for x in sorted(c, key=abs):
        #             if c[x] > c[x * 2]:
        #                 return False
        #             c[x*2] -= c[x]

        #         return True

        A = [abs(num) for num in A]
        A.sort()
        dic = collections.defaultdict(collections.deque)
        for i, num in enumerate(A):
            dic[num].append(i)

        visited = [0] * len(A)
        cnt = 0
        i = 0
        # while cnt < len(A) // 2 :
        while i < len(A):
            if visited[i]:
                i += 1
                continue
            val, val_double = A[i], 2 * A[i]
            if val_double in dic and dic[val_double]:
                if val not in dic or not dic[val]:
                    return False
                dic[val].popleft()
                if not dic[val_double]:
                    return False
                index = dic[val_double].popleft()
                visited[index] = 1

            else:
                return False
            i += 1
            # cnt += 1

        return True

#         A = [abs(num) for num in A ]
#         A.sort()
#         dic = collections.defaultdict(int)
#         for num in A:
#             dic[num] += 1

#         visited = [0]*len(A)
#         cnt = 0
#         i = 0
#         while cnt < len(A) // 2 :
#             if visited[i]:
#                 i += 1
#                 continue
#             val_small = A[i]
#             if 2*val_small in dic:
#                 dic[2*val_small] -= 1
#                 dic[val_small] -= 1
#                 if dic[2*val_small] < 0 or dic[val_small] < 0:
#                     return False
#                 search_index = A.index(2*val_small, i+1)
#                 while visited[search_index]:
#                     search_index = A.index(2*val_small, search_index+1)
#                 visited[search_index] = 1
#             else:
#                 return False
#             i += 1
#             cnt += 1

#         return True
