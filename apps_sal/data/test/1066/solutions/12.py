L = list(input().split())
(n, k) = (int(L[0]), int(L[1]))
if n % 2 == 0:
    if k <= int(n / 2):
        print(2 * k - 1)
    else:
        print(2 * (k - int(n / 2)))
elif k <= int((n + 1) / 2):
    print(2 * k - 1)
else:
    print(2 * (k - int((n + 1) / 2)))
