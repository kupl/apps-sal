n = int(input())

L = list(map(int, input().split()))
a = 0
b = 0

for i in range(n):
    if L[i] % 4 == 0:
        b += 1
    if L[i] % 2 == 1:
        a += 1

if a + b == n and a - b == 1:
    print('Yes')
    return
if b >= a:
    print('Yes')
else:
    print('No')
