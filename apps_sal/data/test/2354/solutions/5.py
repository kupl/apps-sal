(n, q) = list(map(int, input().split()))
Q = [None] * q
for i in range(q):
    Q[i] = list(map(int, input().split()))
for i in range(q):
    x = Q[i][0]
    y = Q[i][1]
    if n % 2 == 0:
        if (x + y) % 2 == 0:
            ANS = (x - 1) * (n // 2) + (y + 1) // 2
        else:
            ANS = n ** 2 // 2 + (x - 1) * (n // 2) + (y + 1) // 2
    elif n % 2 == 1:
        if (x + y) % 2 == 0:
            if x % 2 == 1:
                ANS = (x - 1) // 2 * n + (y + 1) // 2
            else:
                ANS = (x - 1) // 2 * n + (n // 2 + 1) + (y + 1) // 2
        elif x % 2 == 1:
            ANS = n ** 2 // 2 + 1 + (x - 1) // 2 * n + (y + 1) // 2
        else:
            ANS = n ** 2 // 2 + 1 + (x - 1) // 2 * n + n // 2 + (y + 1) // 2
    print(ANS)
