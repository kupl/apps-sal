m = {}
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    m[a[i]] = i
ans = 0
k = 1000000.0
for i in set(a):
    if m[i] < k:
        k = m[i]
        ans = i
print(ans)
