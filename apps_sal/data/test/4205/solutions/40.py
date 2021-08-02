n = int(input())
p = [int(i) for i in input().split()]
cnt = 0
ps = sorted(p)
for i in range(n):
    if p[i] != ps[i]:
        cnt += 1
if cnt in [0, 2]:
    print('YES')
else:
    print('NO')
