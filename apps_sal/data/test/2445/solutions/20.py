t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 1:
        print((n + 1) // 2)
    else:
        print((n + 2) // 2)
