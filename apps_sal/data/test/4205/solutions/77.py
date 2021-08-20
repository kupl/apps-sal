n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(n):
    if i + 1 != p[i]:
        count += 1
if count <= 2:
    print('YES')
else:
    print('NO')
