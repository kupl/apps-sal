N = int(input())
p = list(map(int, input().split()))

count = 0
for i, j in enumerate(p, 1):
    if i != j:
        count += 1
if count <= 2:
    print('YES')
else:
    print('NO')
