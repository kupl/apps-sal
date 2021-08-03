n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = set(list(map(int, input().split())))
ans = []
for i in range(n):
    if a[i] in b:
        ans.append(a[i])
print(*ans)
