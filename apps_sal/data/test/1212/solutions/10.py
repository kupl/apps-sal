(n, k) = map(int, input().split())
t = list(map(int, input().split()))
for i in range(n - 1):
    t[i + 1] += t[i]
t = [0] + t
print(min(((t[i + k] - t[i], i) for i in range(n - k + 1)))[1] + 1)
