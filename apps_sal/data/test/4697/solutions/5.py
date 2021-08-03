n, m = map(int, input().split())

if n >= (m // 2):
    print(m // 2)
else:
    total = n * 2 + m
    print(total // 4)
