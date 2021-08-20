n = int(input())
m = n // 7
n %= 7
ma = m * 2 + min(n, 2)
mi = m * 2
if n > 5:
    mi += n - 5
print(mi, ma)
