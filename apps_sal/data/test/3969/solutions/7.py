(n, m) = list(map(int, input().split()))
t = [int(input().split()[0]) for i in range(n)]
p = [0] * (m + 1)
for i in t:
    p[i] = max(p[1:i + 1]) + 1
print(n - max(p))
