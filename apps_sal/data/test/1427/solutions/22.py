# from fractions import gcd
# P = 10**9+7
# N = int(input())
# S = list(map(int, input().split()))

# l = {2:0}
# for num in S:
#     temp = num
#     M = temp//2+2
#     cnt = 0
#     while temp%2 == 0:
#         cnt += 1
#         temp //= 2
#     l[2] = max(l[2], cnt)
#     i = 3
#     while temp > 1 and i < M:
#         cnt = 0
#         while temp%i == 0:
#             cnt += 1
#             temp //= i
#         if cnt > 0:
#             if i in l:
#                 l[i] = max(l[i], cnt)
#             else:
#                 l[i] = cnt
#         i += 2
#     if temp > 1:
#         if temp in l:
#             l[temp] = max(l[temp], 1)
#         else:
#             l[temp] = 1


# ans = 0
# for i in range(N):
#     ans = (temp//S[i]+ans)%P
# print(ans)


from fractions import gcd
P = 10**9 + 7
N = int(input())
S = list(map(int, input().split()))

temp = S[0]
for i in range(1, N):
    temp = temp * S[i] // gcd(temp, S[i])
temp %= P

ans = 0
for num in S:
    ans = ((temp * pow(num, P - 2, P)) % P + ans) % P
print(ans)
