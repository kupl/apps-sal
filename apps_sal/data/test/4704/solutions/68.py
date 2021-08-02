n = int(input())
A = list(map(int, input().split()))
S = sum(A)
x = A[0]
y = S - x
xy_min = abs(x - y)
for i in range(1, n - 1):
    x += A[i]
    y = S - x
    xy = abs(x - y)
    if xy < xy_min:
        xy_min = xy
print(xy_min)
