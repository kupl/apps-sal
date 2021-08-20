n = int(input())
a = list(map(int, input().split()))
k = max(a)
p = 0
ans = 1
for i in range(n):
    if a[i] == k:
        p += 1
    else:
        ans = max(ans, p)
        p = 0
ans = max(ans, p)
print(ans)
