(N, K) = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * N
point = 1
(m, l) = (0, 0)
if K > N:
    for i in range(N):
        if B[point - 1] == 0:
            B[point - 1] = i + 1
            point = A[point - 1]
        else:
            m = i + 1 - B[point - 1]
            l = B[point - 1]
            break
    if m != 0:
        m = (K - l) % m
    else:
        m = N
else:
    m = K
ans = 1
for i in range(l + m):
    ans = A[ans - 1]
print(ans)
