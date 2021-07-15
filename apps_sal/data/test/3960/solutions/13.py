# n, m = [int(x) for x in input().split(" ")]
# s = set()
# ls = [0]*(n+1)
# in_C = input().split(" ")
#
# for x in range(len(in_C)-1, -1, -1):
#     s.add(int(in_C[x]))
#     ls[x+1] = len(s)
# [print(ls[int(input())]) for i in range(m)]
#
# in_x = input()
# n = list(in_x)
# length = len(n)
# counter = 0
# counter_2 = 0
# for _ in range(length):
#     temp = n[:]
#     if counter > 0:
#         temp.pop(counter)
#     counter += 1
#     for j in range(0, len(temp)):
#         if j > 0:
#             temp.pop((length - 1) - j)
#         num = int("".join(temp))
#         if num % 8 == 0:
#             print(f"YES\n{num}")
#             return
#     temp = n[:]
#     if counter_2 > 0:
#         temp.pop(counter_2)
#     counter_2 += 1
#     # print(temp)
#     for j in range(len(temp), 1, -1):
#         temp.pop(j - len(temp))
#         num = (int("".join(temp)))
#         # print(num)
#         if num % 8 == 0:
#             print(f"YES\n{num}")
#             return
# print("NO")

n = int(input())
nums = input().split(" ")
sumas = [0] * (n+1)
dp = [[0] * 2 for _ in range(n+1)]
res = -1e11
for x in range(0, n):
    if x > 0:
        sumas[x] = abs(int(nums[x]) - int(nums[x - 1]))
for x in range(1, n+1):
    dp[x][0] = max(sumas[x], dp[x - 1][1] + sumas[x])
    dp[x][1] = max(-sumas[x], dp[x - 1][0] - sumas[x])
    res = max(max(dp[x][0], dp[x][1]), res)
print(res)
