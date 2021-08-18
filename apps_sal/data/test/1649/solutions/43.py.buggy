A = list(map(int, input().split()))

sumA = sum(A)
for i in range(2 ** 4):
    tmp = 0
    for j in range(4):
        if (i >> j) & 1:
            tmp += A[j]
    if sumA == tmp * 2:
        print("Yes")
        return

print("No")
