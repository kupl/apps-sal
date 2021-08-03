n = int(input())
a = [0]

for i in range(13):
    for j in range(1, 10):
        a += [int(str(j) + i * '9')]

mx = 0

for i in a:
    if i <= n:
        mx = max(mx, sum(map(int, str(i))) + sum(map(int, str(n - i))))

print(mx)
