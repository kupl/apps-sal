n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in range(a.count(0) + 1):
    zc = 0
    for j in range(n):
        if a[j] == 0:
            zc += 1
        if zc == i:
            break
    ans = max(ans, i + a[j:].count(1))
print(ans)
