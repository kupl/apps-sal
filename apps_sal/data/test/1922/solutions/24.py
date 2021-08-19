n, m = list(map(int, input().split()))

# 遇数回叩かれたら表になる
# 奇数回叩かれたら裏になる

if n == 1 and m == 1:
    print(1)
elif n == 1:
    print(m - 2)
elif m == 1:
    print(n - 2)
else:
    print((n - 2) * (m - 2))
