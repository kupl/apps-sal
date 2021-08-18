n = int(input())
A = list(map(int, input().split()))
a_ = max(A)
A_ = list(set(A))
dp = [True] * (a_ + 1)
C = [0] * (a_ + 1)
for a in A:
    C[a] += 1
A_.sort()
ans = 0

for a in A_:
    tmp = a
    if dp[tmp]:
        tmp += a
        while tmp <= a_:
            dp[tmp] = False
            tmp += a
for a in A_:
    if dp[a]:
        if C[a] == 1:
            ans += 1
print(ans)
