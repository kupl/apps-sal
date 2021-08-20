n = int(input())
a = list(map(int, input().split()))
res = 0
ans = -1
for i in range(n):
    if a[i] >= ans:
        ans = a[i]
    elif a[i] < ans:
        res += ans - a[i]
print(res)
