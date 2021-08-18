N = int(input())
A = list(map(int, input().split()))
x = 0
for a in A:
    x ^= a
idx = 0
for i in range(59, -1, -1):
    if x >> i & 1 == 0:
        for j, a in enumerate(A[idx:], idx):
            if a >> i & 1:
                break
        else:
            continue
        A[idx], A[j] = A[j], A[idx]
        for j in range(N):
            if j != idx and A[j] >> i & 1:
                A[j] ^= a
        idx += 1
s = 0
for a in A:
    s ^= a
for i in range(60):
    if x >> i & 1 == 1 and s >> i & 1:
        s ^= 1 << i
print((x + (s << 1)))
