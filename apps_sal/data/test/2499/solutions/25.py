N = int(input())
A = list(map(int, input().split()))
res = 0
for x in A:
    res ^= x

for i in range(60):
    if (res >> i) & 1:
        for j in range(N):
            if A[j] >> i & 1:
                A[j] ^= 1 << i
start_point = 0
for i in range(60, -1, -1):
    X = 1 << i
    for j in range(start_point, N):
        if A[j] >> i & 1:
            A[start_point], A[j] = A[j], A[start_point]
            for k in range(N):
                if A[k] >> i & 1 and k!=start_point:
                    A[k] ^= A[start_point]
            start_point += 1
            break
plus=0
for x in A:
    plus ^=x
print(res+plus*2)
