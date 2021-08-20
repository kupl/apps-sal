(n, k, x) = list(map(int, input().split()))
times = list(map(int, input().split()))
for i in range(n - 1, n - k - 1, -1):
    times[i] = x
print(sum(times))
