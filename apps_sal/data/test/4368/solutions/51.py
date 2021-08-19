(N, K) = map(int, input().split())
for i in range(10 ** 9):
    if N < K ** i:
        print(i)
        break
