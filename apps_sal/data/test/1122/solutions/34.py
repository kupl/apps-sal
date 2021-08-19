(N, M) = map(int, input().split())
if N % 2:
    for i in range(M):
        print(i + 1, M * 2 - i)
else:
    b = M // 2
    a = M - b
    for i in range(a):
        print(i + 1, a * 2 - i)
    for i in range(b):
        print(a * 2 + 1 + i, M * 2 + 1 - i)
