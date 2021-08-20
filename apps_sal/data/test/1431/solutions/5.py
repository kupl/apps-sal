n = int(input())
a = list(map(int, input().split()))
ans = [False] * n
for i in range(n // 2, n):
    ans[i] = a[i]
for i in range(n // 2 - 1, -1, -1):
    mod = False
    for j in range(i, n, i + 1):
        if ans[j] == 1:
            mod = not mod
    mod = 1 if mod else 0
    ans[i] = True if mod != a[i] else False
cnt = 0
ind = []
for i in range(n):
    if ans[i] == True:
        cnt += 1
        ind.append(i + 1)
print(cnt)
if cnt > 0:
    print(' '.join(map(str, ind)))
