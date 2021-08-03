N, L = list(map(int, input().split()))
if L > 0:
    print((sum(L + i for i in range(1, N))))
elif L + N - 1 < 0:
    print((sum(L + i for i in range(N - 1))))
else:
    print((sum(L + i for i in range(N))))
