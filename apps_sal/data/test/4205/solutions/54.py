x = int(input())
p = list(map(int, input().strip().split()))
k = sorted(p)
count = 0
for i in range(0,x):
    if p[i] == k[i]:
        count += 1

if (x - count) == 2 or (x - count) == 0:
    print('YES')
else:
    print('NO')

