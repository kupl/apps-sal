N = int(input())
p = list(map(int, input().split()))
count = 0
for n in range(N):
    if n + 1 != p[n]:
        count += 1
if count in [0, 2]:
    print('YES')
else:
    print('NO')
