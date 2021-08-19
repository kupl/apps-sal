import math
N = int(input())
C = []
S = []
F = []
for _ in range(N - 1):
    (c, s, f) = list(map(int, input().split()))
    C.append(c)
    S.append(s)
    F.append(f)
for i in range(N - 1):
    count = 0
    count += S[i]
    count += C[i]
    for j in range(i + 1, N - 1):
        if count < S[j]:
            count = S[j]
        else:
            count = math.ceil((count - S[j]) / F[j]) * F[j] + S[j]
        count += C[j]
    print(count)
print(0)
