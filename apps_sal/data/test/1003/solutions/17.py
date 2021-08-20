(n, m) = list(map(int, input().split()))
t = 0
while n != 0:
    n = n - 1
    t = t + 1
    if t % m == 0:
        n = n + 1
print(t)
