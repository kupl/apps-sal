(n, L) = tuple(map(int, input().split()))
kefa = list(map(int, input().split()))
sasha = list(map(int, input().split()))
(diffsk, diffss) = ([], [])
for k in range(n):
    diffsk.append(kefa[k % n] - kefa[(k - 1) % n])
    diffss.append(sasha[k % n] - sasha[(k - 1) % n])
res = False
for j in range(n):
    tmp = True
    diff = (diffsk[0] - diffss[j]) % L
    for i in range(n):
        if (diffsk[i] - diffss[(i + j) % n]) % L != diff:
            tmp = False
    if tmp:
        res = True
if res:
    print('YES')
else:
    print('NO')
