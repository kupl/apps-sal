# class Solution:
#     def maxDistance(self, position: List[int], m: int) -> int:
#         #首先排序
#         position.sort()
#         print(position)

#         left = 1000000000
#         right = position[-1] - position[0]
#         for i in range(len(position)-1):
#             diff = abs(position[i] - position[i+1])
#             left = min(left, diff)


#         def check(diff, p, m):
#             m -= 1
#             last = p[0]
#             for i in range(1, len(p)):
#                 if abs(p[i] - last) >= diff:
#                     m -= 1
#                     last = p[i]
#                     if m <= 0:
#                         print(diff, \"True\")
#                         return True
#                 else:
#                     pass
#             print(diff, \"False\")
#             return False

#         print(\"left\", left, \"right\", right)
#         while left < right:
#             mid = (left + right) // 2
#             if check(mid, position, m) == True:
#                 left = mid
#                 if left == right:
#                     print(\"find 1\", left)
#                     break
#                 if left + 1 == right:
#                     if check(right, position, m):
#                         left = right
#                         print(\"find 2\", left)
#                     break
#             else:
#                 right = mid - 1


#         print(\"find 3\", left)
#         return left

# class Solution:
#     def maxDistance(self, position: List[int], m: int) -> int:
#         #首先排序
#         position.sort()
#         # print(position)

#         distance = [0 for _ in range(len(position)-1)]
#         for i in range(len(position)-1):
#             diff = position[i+1] - position[i]
#             distance[i] = diff
#         left = min(distance)
#         right = ceil((position[-1] - position[0]) / (m-1))

#         def check(diff, m):
#             m -= 1
#             pre_dis = 0
#             for i in range(0, len(distance)):
#                 if distance[i]+pre_dis >= diff:
#                     m -= 1
#                     if m <= 0:
#                         # print(diff, \"True\")
#                         return True
#                     pre_dis = 0
#                 else:
#                     pre_dis += distance[i]
#             # print(diff, \"False\")
#             return False

#         # print(\"left\", left, \"right\", right)
#         while left < right:
#             mid = (left + right+1) // 2
#             if check(mid, m) == True:
#                 left = mid
#                 # if left == right:
#                 #     print(\"find 1\", left)
#                 #     break
#                 # if left + 1 == right:
#                 #     if check(right, position, m):
#                 #         left = right
#                 #         print(\"find 2\", left)
#                 #     break
#             else:
#                 right = mid - 1


#         # print(\"find 3\", left)
#         return left

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        result = 0

        # can we place m balls each separated by x distance?
        def check(x) -> bool:
            nonlocal position, m

            last = position[0]
            placed = 1
            for pos in position:
                if pos - last >= x:
                    placed += 1
                    if placed >= m:
                        return True
                    last = pos

            return False

        first = 0
        last = int(ceil((position[-1] - position[0]) / (m - 1)))
        while first < last:

            mid = (first + last + 1) // 2

            if check(mid):
                result = mid
                first = mid
            else:
                last = mid - 1

        return first
