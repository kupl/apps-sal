N, M= map(int, input().split())

if N >= M // 2:
    print(M // 2)

else:
    m = M - N * 2
    s = m // 4
    print(N + s)
