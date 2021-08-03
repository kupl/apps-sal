A = list(map(int, input().split()))
l = A[0]
r = A[1]
n = 0
for i in range(0, 33):
    for j in range(0, 33):
        cur = pow(2, i) * pow(3, j)
        if (cur >= l and cur <= r):
            n += 1
print(n)
