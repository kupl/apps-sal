N = int(input())
d = [int(input()) for _ in range(N)]
d.sort()
ans = N
for i in range(N - 1):
    if d[i] == d[i + 1]:
        ans -= 1
print(ans)
