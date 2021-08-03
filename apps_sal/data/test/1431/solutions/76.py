n = int(input())
A = list(map(int, input().split()))

dp = [0] * (n + 2)
A = [0] + A

for i in range(n, 0, -1):
    tmp = 0
    # print(i)
    for j in range(i, n + 1, i):
        # print(i,j)
        tmp += dp[j]
    # print(111,tmp,A[i],i)
    if A[i] != (tmp % 2):
        # print(i)
        dp[i] = 1
l = []
# print(dp)
for i in range(1, n + 1):
    if dp[i] == 1:
        l.append(i)
if len(l) == 0:
    print(len(l))
else:
    print(len(l))
    print(*l)
