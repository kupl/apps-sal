N = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(N):
    if p[i] == i + 1:
        if i != N - 1 and p[i + 1] == i + 2:
            p[i + 1] = p[i]
        ans += 1
print(ans)
