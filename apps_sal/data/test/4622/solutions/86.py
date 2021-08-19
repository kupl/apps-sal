n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
memo = 0
for i in range(n - 1):
    if b[i] == b[i + 1]:
        memo += 1
if memo == 0:
    print('YES')
else:
    print('NO')
