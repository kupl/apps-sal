def R(): return map(int, input().split())


n, I = R()
a = sorted(R())
b = [0] + [i + 1for i in range(n - 1)if a[i] < a[i + 1]]
print(n - max(y - x for x, y in zip(b, b[1 << 8 * I // n:] + [n])))
