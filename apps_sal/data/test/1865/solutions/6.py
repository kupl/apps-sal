import bisect
n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    j = min(list(range(i, n)), key=lambda k: a[k])
    if j != i:
        (a[i], a[j]) = (a[j], a[i])
        ans.append((i, j))
print(len(ans))
for (i, j) in ans:
    print(i, j)
