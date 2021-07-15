n, k = map(int, input().split())
a = (n - k) // 2
s = '0' * a + '1'
print(s * (n // (a + 1)) + s[:n % (a + 1)])
