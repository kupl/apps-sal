n = int(input())
b = []
for i in range(n):
    (tl, tr) = list(map(int, input().split()))
    b.append((tl, tr))
k = int(input())
ans = 0
for (l, r) in b:
    if k <= r:
        ans += 1
print(ans)
