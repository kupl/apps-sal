n, k = list(map(int, input().split()))

if n < 3 * k:
    print(-1)

else:

    d = n // k - 1

    t = list(str(i) + ' ' for i in range(1, k + 1))

    print(''.join(t) + ''.join(i * d for i in t) + t[-1] * (n - (d + 1) * k))


# Made By Mostafa_Khaled
