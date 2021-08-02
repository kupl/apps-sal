A, B, C, D = map(int, input().split())

if B <= C or D <= A:
    print(0)
else:
    min_n = max(A, C)
    max_n = min(B, D)
    print(max_n - min_n)
