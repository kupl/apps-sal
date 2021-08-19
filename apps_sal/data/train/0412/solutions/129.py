class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # dp(depth, f, target) = 1+dp(depth-1, f, target-face_chosen) for f_c in range(1,f+1)

        opt = [[0] * (target + 1) for _ in range(d + 1)]
        opt[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                # we need to get sum of all arrows out
                sum_children = 0
                face_val = 1
                while face_val <= f and j - face_val >= 0:
                    sum_children += opt[i - 1][j - face_val] % mod
                    face_val += 1
                opt[i][j] = sum_children % mod
        # print(opt[1])
        # print(opt[0])
        return opt[d][target]


#         for d in range()


#         opt(i, j) = 1+sum(opt(i-1, j-face) for face in range(1, f+1))


#         we want opt(d=d, f=f, sum_=target)


#         prev_map = dict()
#         for face in range(2, f+1):
#             prev_map[face]=1

#         for dice in range(1, d+1):
#             new_map = dict()
#             for face in range(1, face):
#                 for i, count in prev_map.items():
#                     new_map[face+i]=count+i
#             new_map = prev_map

#         print(prev_map)
#         return prev_map[target]
