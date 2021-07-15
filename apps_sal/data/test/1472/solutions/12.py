N, X, Y = map(int, input().split())

res = [0]*(N-1)

for i in range(1, N+1):
    for j in range(i+1, N+1):
        # i -> j
        d1 = abs(j - i)
        # i -> X -> Y -> j
        d2 = abs(X-i) + abs(Y-j) + 1
        # i -> Y -> X -> j
        d3 = abs(Y-i) + abs(X-j) + 1

        min_d = min(d1, d2, d3)
        res[min_d-1] += 1

print(*res, sep='\n')

