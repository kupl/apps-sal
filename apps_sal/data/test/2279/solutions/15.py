n = int(input())
ans = [0] * (n * 2 + 1)
used = [False] * (n * 2 + 1)
arr = []
for i in range(2, n * 2 + 1):
    qwe = [0] + [int(x) for x in input().split()]
    for j in range(1, i):
        arr.append((qwe[j], i, j))
arr.sort(reverse=True)
for x in arr:
    if not used[x[1]] and (not used[x[2]]):
        used[x[1]] = used[x[2]] = True
        ans[x[1]] = x[2]
        ans[x[2]] = x[1]
print(*ans[1:])
