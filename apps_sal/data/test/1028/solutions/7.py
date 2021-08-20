(n, m) = list(map(int, input().split()))
maxx = (n - m + 1) * (n - m) // 2
x = n // m
minn = x * (x - 1) // 2
minn *= m
minn += x * (n % m)
print(minn, maxx)
