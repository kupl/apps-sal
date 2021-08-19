(n, m) = [int(i) for i in input().split()]
for i in reversed(list(range(0, n // 2 + 1))):
    s = i + n - 2 * i
    if s % m == 0:
        print(s)
        break
else:
    print(-1)
