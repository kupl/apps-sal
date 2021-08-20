(m, n) = map(int, input().split())
t = [pow(1 - i / m, n) for i in range(m + 1)]
print(sum(((t[i] - t[i + 1]) * (m - i) for i in range(m))))
