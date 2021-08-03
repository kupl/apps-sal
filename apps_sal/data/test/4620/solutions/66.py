N = int(input())
T = 0
t = 0
ans = []
for i in range(N - 1):
    C, S, F = list(map(int, input().split()))
    for j in range(len(ans)):
        if ans[j] <= S:
            ans[j] = S + C
        elif ans[j] % F != 0:
            ans[j] = ans[j] + F - (ans[j] % F) + C
        else:
            ans[j] += C
    ans.append(S + C)
for a in ans:
    print(a)
print((0))
