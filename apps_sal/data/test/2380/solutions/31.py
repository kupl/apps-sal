(N, M) = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]
A.sort()
BC.sort(key=lambda x: x[1], reverse=True)
k = 0
for (b, c) in BC:
    i = 0
    for j in range(b):
        if A[k] < c and i <= b:
            A[k] = c
            if k == N - 1:
                break
            k += 1
            i += 1
    if k == N - 1 or A[k] >= c:
        break
print(sum(A))
