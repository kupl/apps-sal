(A, B, K) = list(map(int, input().split()))
SA = list(range(A, min(B, A + K)))
SB = list(range(max(A, B - K + 1), B + 1))
ans = sorted(set(SA + SB))
for a in ans:
    print(a)
