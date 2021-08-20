import itertools as itt
(n, m) = map(int, input().split())
l = set()
for i in range(m):
    (a, b) = map(int, input().split())
    l.add((a, b))
    l.add((b, a))
lis = [i for i in range(1, n + 1)]
p_lis = list(itt.permutations(lis))
cnt = 0
for i in range(len(p_lis)):
    if p_lis[i][0] != 1:
        continue
    flg = [0] * (n - 1)
    for j in range(n - 1):
        x = (p_lis[i][j], p_lis[i][j + 1])
        if x in l:
            flg[j] = 1
    if all(flg):
        cnt += 1
print(cnt)
