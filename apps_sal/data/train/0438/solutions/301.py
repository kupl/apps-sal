class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        n = len(arr)
        que = collections.deque([(1, n)])

        for i in range(n - 1, -1, -1):

            k = len(que)

            for j in range(k):
                l, r = que.popleft()
                if r - l + 1 == m:
                    return i + 1

                if l <= arr[i] <= r:
                    if arr[i] - l >= m:
                        que.append((l, arr[i] - 1))
                    if r - arr[i] >= m:
                        que.append((arr[i] + 1, r))
                else:
                    que.append((l, r))
        return -1

        # change endpoint .
        # n = len(arr)
        # if m == n:
        #     return m
        # length = [0] * (n+2)
        # # count = [0] * (n+1)
        # res = -1
        # for i, num in enumerate(arr):
        #     left = length[num-1]
        #     right = length[num + 1]
        #     # I almost came up with this, change the endpoint.
        #     length[num-left] = length[num+right] = left+right+1
        #     if left == m or right == m:
        #         res = i
        # return res

    # if m == len(A): return m
    #     length = [0] * (len(A) + 2)
    #     res = -1
    #     for i, a in enumerate(A):
    #         left, right = length[a - 1], length[a + 1]
    #         if left == m or right == m:
    #             res = i
    #         length[a - left] = length[a + right] = left + right + 1
    #     return res

        # Union-find
#         n = len(arr)
#         p = [i for i in range(n+1)]
#         count = [0] * (n+1)
#         ### I didn't come up with this groups at first. It shouldn't be hard.
#         groups = [0] * (n+1)
#         def findp(x):
#             while x != p[x]:
#                 x = p[x]
#             return x

#         def union(x, y):

#             groups[count[y]] -= 1
#             groups[count[x]] -= 1
#             if count[x] >= count[y]:
#                 p[y] = x
#                 count[x] += count[y]
#                 groups[count[x]] += 1
#             else:
#                 p[x] = y
#                 count[y] += count[x]
#                 groups[count[y]] += 1

#         res = -1

#         for i, num in enumerate(arr):
#             # print(p)
#             # print(count)
#             count[num] = 1
#             left = num-1
#             right = num + 1
#             groups[1] += 1
#             if left >= 1 and count[left] != 0:
#                 pl = findp(left)
#                 pm = findp(num)
#                 if pl != pm:
#                     union(pl, pm)
#             if right <= n and count[right] != 0:
#                 pr = findp(right)
#                 pm = findp(num)
#                 if pr != pm:
#                     union(pr, pm)

#             if groups[m] > 0:
#                 res = i+1
#         return res
