n, m = map(int, input().split())
a = list(map(int, input().split()))

v = [0] * (m + 1)

for i in a:
    v[i] += 1

an = n * (n - 1) // 2

for i in v:
    an -= i * (i - 1) // 2

print(an)
