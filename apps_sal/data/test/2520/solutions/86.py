import sys
sys.setrecursionlimit(10**5)

n,m,k = list(map(int, input().split()))

F = [[] for _ in range(n+1)]
B = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = list(map(int, input().split()))
    F[x].append(y)
    F[y].append(x)

for _ in range(k):
    x,y = list(map(int, input().split()))
    B[x].append(y)
    B[y].append(x)

belongs = [-1 for _ in range(n+1)]
group_ID = 0

def f_search(root, group_ID):
    for j in F[root]:
        if belongs[j] == -1:
            belongs[j] = group_ID
            f_search(j, group_ID)

for i in range(n+1):
    if belongs[i] == -1:
        belongs[i] = group_ID
        f_search(i, group_ID)
        group_ID += 1

cnt_members = [0 for _ in range(len(set(belongs)))]
for i in belongs[1:]:
    cnt_members[i] += 1

ans = [0 for _ in range(n+1)]
for i in range(1, n+1):
    tmp = 0
    for j in B[i]:
        if belongs[j] == belongs[i]:
            tmp += 1
    ans[i] = cnt_members[belongs[i]] - 1 - len(F[i]) - tmp

print((*ans[1:]))

