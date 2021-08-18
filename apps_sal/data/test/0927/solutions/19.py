N, M = map(int, input().split())
A = list(map(int, input().split()))

T = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
B = []
for i in A:
    B.append(T[i])
B = sorted(list(set(B)))
dp = [0 for i in range(N + 1)]
AB = [[i, T[i]] for i in A]
AB = sorted(AB, reverse=True)

for i in range(1, N + 1):
    for j in B:
        if i - j >= 0 and dp[i - j] != -1:
            dp[i] = max(dp[i], dp[i - j] + 1)
    if dp[i] == 0:
        dp[i] = -1

c = N
U = [0 for i in range(8)]
while c > 0:
    for i in range(len(AB)):
        if c - AB[i][1] >= 0 and dp[c] == dp[c - AB[i][1]] + 1:
            U[AB[i][1]] += 1
            c -= AB[i][1]
            break

ans = ""
if 9 in A:
    ans += '9' * U[6]
    U[6] = 0
if 8 in A:
    ans += '8' * U[7]
if 7 in A:
    ans += '7' * U[3]
if 6 in A:
    ans += '6' * U[6]
if 5 in A:
    ans += '5' * U[5]
    U[5] = 0
if 4 in A:
    ans += '4' * U[4]
if 3 in A:
    ans += '3' * U[5]
    U[5] = 0
if 2 in A:
    ans += '2' * U[5]
if 1 in A:
    ans += '1' * U[2]

print(ans)
