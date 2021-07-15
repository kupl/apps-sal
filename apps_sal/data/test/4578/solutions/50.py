N, X = list(map(int, input().split()))
M = [int(input()) for _ in range(N)]

min_M = min(M)
sum_M = sum(M)

print((N+((X-sum_M)//min_M)))

