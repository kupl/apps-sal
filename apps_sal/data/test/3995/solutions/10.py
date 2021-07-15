n, k = map(int, input().split())

x = (n - k) // 2
f = ('0' * x) + '1'

f = f * ((n // (x+1)) + 1)
print(f[:n])
