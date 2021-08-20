(n, k) = list(map(int, input().split()))
s = 0
for i in range(k, n + 2):
    s += i * (n * 2 + 1 - i) // 2 - i * (i - 1) // 2 + 1
print(s % 1000000007)
