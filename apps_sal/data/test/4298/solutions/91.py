(N, D) = map(int, input().split())
for n in range(1, 25):
    if N <= (2 * D + 1) * n:
        print(n)
        break
