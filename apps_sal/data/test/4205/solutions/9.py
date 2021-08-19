n = int(input())
lst = list(map(int, input().split()))
c = 0
for i in range(n):
    if lst[i] != i + 1:
        c = c + 1
if c <= 2:
    print('YES')
else:
    print('NO')
