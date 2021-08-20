a = input()
N = int(a)
p = list(map(int, input().split()))
count = 0
for i in range(N):
    if p[i] != i + 1:
        count = count + 1
    if count == 3:
        break
if count == 3:
    print('NO')
else:
    print('YES')
