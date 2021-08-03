n, k = map(int, input().split())
d = 0
t = sum(((i - 1) // k + 1) for i in map(int, input().split()))
print((t - 1) // 2 + 1)
