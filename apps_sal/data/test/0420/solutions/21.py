n, m = map(int, input().split())
a = [int(input()[::2], 2) for i in range(n)]
if n & 1:
    print(n)
else:
    k = n // 2
    while True:
        if a[:k] != a[k:k * 2][::-1]:
            print(k * 2)
            break
        elif k & 1:
            print(k)
            break
        k //= 2
