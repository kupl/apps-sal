from itertools import product
n = int(input())
p = 2
iterator = product(range(p), repeat=n)

L = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        L[i].append(list(map(int, input().split())))
ans = 0
for idxs in iterator:
    cnt_honest = 0
    for i in range(n):
        cnt = 0
        if idxs[i] == 1:
            for j in L[i]:
                if idxs[j[0] - 1] == j[1]:
                    cnt += 1
            if cnt == len(L[i]):
                cnt_honest += 1
    if cnt_honest == sum(idxs):
        ans = max(sum(idxs), ans)
print(ans)
