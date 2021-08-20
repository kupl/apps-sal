A = list(map(int, input().split()))
f = 0
for i in range(1 << 4):
    c = 0
    for j in range(4):
        if i >> j & 1:
            c += A[j]
    if sum(A) / 2 == c:
        f = 1
if f:
    print('Yes')
else:
    print('No')
