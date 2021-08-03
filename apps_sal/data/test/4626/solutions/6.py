q = int(input())
for i in range(q):
    [a, b, c] = list(map(int, input().rstrip().split()))
    mi = min(a, b, c)
    ma = max(a, b, c)
    altro = a + b + c - mi - ma
    if mi == ma:
        print(0)
    elif ma - mi == 1:
        print(0)
    else:
        mi += 1
        ma -= 1
        print(2 * (ma - mi))
