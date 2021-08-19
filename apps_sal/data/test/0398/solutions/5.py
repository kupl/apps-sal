n = int(input())
A = sorted([int(x) for x in input().split()])
found = False
for i in range(n - 2):
    if A[i] + A[i + 1] > A[i + 2]:
        found = True
if found:
    print('YES')
else:
    print('NO')
