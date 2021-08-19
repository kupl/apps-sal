n = int(input())
l = [[] for _ in range(n)]
li = []
for i in range(n - 1):
    (a, b) = map(int, input().split())
    l[a - 1].append(b - 1)
    li.append([a - 1, b - 1])
ans = [-1] * n
for i in range(n):
    x = 0
    for (j, h) in enumerate(l[i]):
        if ans[i] == j:
            x += 1
        ans[h] = j + x
print(max(ans) + 1)
for i in range(n - 1):
    print(ans[li[i][1]] + 1)
