n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
a = list(map(int, input().split()))
ans, st = 0, 0
for i in range(n):
    if a[st] >= c[i]:
        ans += 1
        st += 1
    if st >= m:
        break
print(ans)

