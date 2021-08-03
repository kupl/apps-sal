N, T = list(map(int, input().split()))
t = list(map(int, input().split()))
t.append(float('inf'))
ans = 0
for i in range(len(t) - 1):
    ans += min(T, t[i + 1] - t[i])
print(ans)
