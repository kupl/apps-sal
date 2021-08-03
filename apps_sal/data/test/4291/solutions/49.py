N, K = list(map(int, input().split()))
moji = str(input())
ans = [0]
for i in range(N - 1):
    if moji[i] == "A" and moji[i + 1] == "C":
        ans.append(ans[i] + 1)
    else:
        ans.append(ans[i])


for i in range(K):
    st, sp = list(map(int, input().split()))
    print((ans[sp - 1] - ans[st - 1]))
