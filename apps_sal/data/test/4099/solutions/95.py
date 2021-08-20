(N, K, M) = map(int, input().split())
arr = list(map(int, input().split()))
num = sum(arr)
ideal = N * M
sa = ideal - num
if sa > K:
    print(-1)
elif sa <= 0:
    print(0)
else:
    print(sa)
