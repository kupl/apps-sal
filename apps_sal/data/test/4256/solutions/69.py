a, b, c = list(map(int, input().split()))

oto = b // a
if oto <= c:
    print(oto)
elif oto > c:
    print(c)
