n, t = int(input()), [0] + list(map(int, input().split()))
a, b = map(int, input().split())

for i in range(1, n + 1):
    t[i] += t[i - 1]

if a > b:
    a, b = b, a
a, b = a - 1, b - 1
print(min(t[b] - t[a], t[a] + t[n] - t[b]))
