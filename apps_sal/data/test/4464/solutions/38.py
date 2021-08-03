a, b, c = map(int, input().split())
A = []
for i in range(1, b + 1):
    mod = a * i % b
    if mod in A:
        break
    A.append(mod)

A.sort()
if len(A) >= 2:
    i = A[1]
else:
    i = 0

if i == 0 and c == 0:
    print('YES')
    return
elif i == 0 and c != 0:
    print('NO')
    return

if c % i == 0:
    print('YES')
else:
    print('NO')
