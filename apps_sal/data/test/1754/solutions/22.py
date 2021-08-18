n, m, k = map(int, input().split())
strong = list(map(int, input().split()))
sch = list(map(int, input().split()))
best = list(map(int, input().split()))
arr = [[] for i in range(m + 1)]
for i in range(n):
    arr[sch[i]].append((i, strong[i]))

S = set()
for el in best:
    S.add(el)
M = set()
for i in range(len(arr)):
    max_ = -100000
    pup = -1
    for j in range(len(arr[i])):
        if arr[i][j][1] > max_:
            max_ = arr[i][j][1]
            pup = arr[i][j][0]
    M.add(pup + 1)
for el in M:
    if el in S:
        S.remove(el)
print(len(S))
