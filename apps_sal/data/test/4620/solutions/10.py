N = int(input())
x = []
for i in range(N - 1):
    (c, s, f) = list(map(int, input().split()))
    x.append([c, s, f])
ans = []
for i in range(N - 1):
    t = x[i][0] + x[i][1]
    for j in range(i + 1, N - 1):
        if t % x[j][2] == 0:
            t = max(t, x[j][1])
        else:
            t = max(t + (x[j][2] - t % x[j][2]), x[j][1])
        t += x[j][0]
    ans.append(t)
ans.append(0)
for i in range(N):
    print(ans[i])
