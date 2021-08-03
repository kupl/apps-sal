N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans = 0
for i in range(N):
    t = 0
    for j in range(0, min(N, i + 1)):
        t += A1[j]
    for k in range(i, N):
        t += A2[k]
    ans = max(t, ans)
print(ans)
