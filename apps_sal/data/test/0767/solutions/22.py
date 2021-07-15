N, Z = list(map(int, input().split()))
A = sorted([int(a) for a in input().split()])
l, r = 0, N//2+1
while r - l > 1:
    m = (r+l) // 2
    for i in range(m):
        if A[N-m+i] - A[i] < Z:
            r = m
            break
    else:
        l = m
print(l)

