N = int(input())
p = list(map(int, input().split()))
sp = sorted(p)
count = 0
for i in range(N):
    if p[i] != sp[i]:
        count += 1
if count == 2 or count == 0:
    print('YES')
else:
    print('NO')
