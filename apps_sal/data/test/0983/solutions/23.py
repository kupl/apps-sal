# -------------INPUT---------------------------
n, p, q, r = [int(i) for i in input().split(" ")]
a = input()

b = a.split()

for i in range(n):
    b[i] = int(b[i])

# ---------------------------------------------

dp = [p * b[0]]
for i in range(1, n):
    dp.append(max(dp[i - 1], p * b[i]))
# print(dp)

dq = [dp[0] + q * b[0]]
for i in range(1, n):
    dq.append(max(dq[i - 1], dp[i] + q * b[i]))
# print(dq)

dr = [dq[0] + r * b[0]]
for i in range(1, n):
    dr.append(max(dr[i - 1], dq[i] + r * b[i]))

print(dr[-1])
#  i = 0
# while i < len(a):
#     if a[i] == ' ':
#         i += 1
#     if a[i] == '-':
#         b.append(int(a[i]+a[i+1]))
#         i += 2
#     else:
#         b.append(int(a[i]))
#         i += 1
# print(b)
# num = [p,q,r]
# l = []
# sum = p * b[0] + q * b[0] + r * b[0]
# x = len(b)
# for i in range(x):
#     for j in range(i, x):
#         for k in range(j, x):
#             # print(i,j,k)
#             sum = max(sum, p * b[i] + q * b[j] + r * b[k])
#
# # print(sum)
#
#
# # def indiceb(b):
# #     for i in range(len(b)):
# #         if b[i] == max(b):
#             return i
#
#
# def indices(b):
#     for i in range(len(b)):
#         if b[i] == min(b):
#             return i
#
# if p > 0:
#     sum += max(b) * p
# if p < 0:
#     sum += min(b) * p
#
# if q > 0:
#     sum += max(b[indices(b):]) * q
# if q < 0:
#     sum += min(b) * q
#
# #
# for ii in range(3):
#     if num[ii] >= 0:
#         sum += max(b)*num[ii]
#     if num[ii] < 0:
#         sum += min(b)*num[ii]
