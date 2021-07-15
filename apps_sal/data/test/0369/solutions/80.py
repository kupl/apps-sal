N, M = list(map(int, input().split()))
S = input()
S = S[::-1]

dp = [-1] * (N+1)
dp[0] = 0

pos = 0
while pos < N:

    p = pos
    update = False

    for i in range(1, M + 1):
        if p + i > N:
            break
        if S[p + i] == "0":
            update = True
            pos = p + i
            dp[pos] = dp[p] + 1

    if not update:
        break

if dp[N] == -1:
    print((-1))
    return

dp = dp[::-1]
num = dp[0]
ans = []
pos = 0

while num > 0:
    for i in range(1, M + 1):
        if dp[pos + i] == num - 1:
            num -= 1
            pos += i
            ans.append(str(i))
            break

ans = " ".join(ans)
print(ans)

