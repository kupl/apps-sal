
N, K = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))

S = input()
li = [1] * (K)
ans = [0, 0, 0]

for i in range(N - K):
    if S[i] == S[i + K]:
        li[i % K] += 1
    else:
        if S[i] == "r":
            ans[0] += (li[i % K] + 1) // 2
        if S[i] == "s":
            ans[1] += (li[i % K] + 1) // 2
        if S[i] == "p":
            ans[2] += (li[i % K] + 1) // 2
        li[i % K] = 1


for j in range(N - K, N):
    if S[j] == "r":
        ans[0] += (li[j % K] + 1) // 2
    if S[j] == "s":
        ans[1] += (li[j % K] + 1) // 2
    if S[j] == "p":
        ans[2] += (li[j % K] + 1) // 2


print((p * ans[0] + r * ans[1] + s * ans[2]))
