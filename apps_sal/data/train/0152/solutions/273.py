class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        L = len(position)

        left = 1
        right = position[-1] - position[0]

        def can_place(f):
            n_ball = m - 1
            cum_dis = 0
            p = 1
            #n_ball -= 1
            while n_ball > 0 and p < L:
                cum_dis += position[p] - position[p - 1]
                if cum_dis >= f:
                    n_ball -= 1
                    cum_dis = 0
                p += 1

            if n_ball == 0:
                return True
            else:
                return False

        # return can_place(4)
        # 1, 9, 5 false
        # 1, 4, 2, true
        # 2, 4, 3, true
        # 3, 4, 3,

        while left < right:
            mid = (left + right) // 2
            if can_place(mid):
                left = mid
            else:
                right = mid - 1
            if right - left == 1:
                if can_place(right):
                    return right
                else:
                    return left

        # return can_place(3)
        return left

#         if m == 2:
#             return position[-1] - position[0]

#         L = len(position)

#         hp = []
#         f_set = {}
#         b_set = {}
#         for i in range(L-1):
#             heapq.heappush(hp, (position[i+1]-position[i], position[i], position[i+1]))
#             f_set[position[i]] = position[i+1]
#             b_set[position[i+1]] = position[i]

#         total = L-1

#         while total > m-1:
#             l, x, y = heapq.heappop(hp)
#             if x in f_set and y in b_set and f_set[x] == y and b_set[y] == x:
#                 left_len = float(inf)
#                 right_len = float(inf)
#                 if y in f_set:
#                     right_len = f_set[y]-y
#                 if x in b_set:
#                     left_len = x-b_set[x]
#                 if left_len < right_len:
#                     #merge with left
#                     new_y = y
#                     new_x = b_set[x]
#                     del f_set[x]
#                     del b_set[x]
#                     f_set[new_x] = new_y
#                     b_set[new_y] = new_x
#                     ret = new_y - new_x
#                 else:
#                     # merge with right
#                     new_y = f_set[y]
#                     new_x = x
#                     del f_set[y]
#                     del b_set[y]
#                     f_set[new_x] = new_y
#                     b_set[new_y] = new_x
#                     ret = new_y - new_x
#                 heapq.heappush(hp, (new_y-new_x, new_x, new_y))
#                 total -= 1

#         ret = float(inf)
#         for k in f_set.keys():
#             ret = min(ret, f_set[k]-k)

#         return f_set
