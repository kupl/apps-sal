m, n = input().split()
n = int(n)
m = int(m)
if n > m:
    n, m = m, n
print(n, int((m - n) // 2))
