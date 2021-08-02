A, B, C, D = map(int, input().split())

if A * B >= C * D:
    print(A * B)
if A * B < C * D:
    print(C * D)
