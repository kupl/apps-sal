(n, x) = map(int, input().split())
A = list(map(int, input().split()))
c = 0
ans = 0
for i in A:
    if i < x:
        c += 1
    if i == x:
        ans += 1
ans += x - c
print(ans)
