def R():
    return map(int, input().split())


(n, I) = R()
a = (-1, *sorted(R()))
b = [i for i in range(n) if a[i] < a[i + 1]]
print(n - max((y - x for (x, y) in zip(b, b[1 << 8 * I // n:] + [n]))))
