(n, m) = map(int, input().split())
a = [False] * m
n %= m
while a[n] == False:
    a[n] = True
    n = (n + n) % m
print('Yes') if a[0] else print('No')
