n, k = map(int, input().split())

div_size = n // k

if div_size < 3:
    print(-1)
else:
    keepers = []

    for i in range(k):
        keepers.append(i + 1)

    for i in range(k):
        for _ in range(div_size - 1):
            keepers.append(i + 1)

    shortage = n - len(keepers)

    for _ in range(shortage):
        keepers.append(k)

    print(*keepers)
