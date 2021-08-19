n = int(input())
P = list(map(int, input().split()))
Psort = sorted(P)
cnt = 0
for i in range(n):
    if P[i] != Psort[i]:
        cnt += 1
if cnt <= 2:
    print('YES')
else:
    print('NO')
