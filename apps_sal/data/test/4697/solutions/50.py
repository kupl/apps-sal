(n, m) = list(map(int, input().split()))
if m // 2 >= n:
    print(n + (m // 2 - n) // 2)
else:
    print(m // 2)
