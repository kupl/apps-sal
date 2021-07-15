N = int(input())
d = [int(input()) for i in range(N)]
d.sort(reverse=True)
ans = 0
ind = 100000
for i in range(N):
    if d[i] < ind:
        ans += 1
        ind = d[i]
print(ans)
