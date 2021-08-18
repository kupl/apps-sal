def read(): return list(map(int, input().split()))


n = int(input())
a = list(read())
wasr = [False] * n
wasl = [False] * n
cnt = 0
inf = 10 ** 9
for i in range(n):
    if wasl[i]:
        continue
    wasl[i] = True
    cur = a[i]
    Min = inf
    ind = -1
    for j in range(n):
        if wasr[j]:
            continue
        if cur < a[j] < Min:
            Min = a[j]
            ind = j
    if ind != -1:
        wasr[ind] = True
        cnt += 1
print(cnt)
