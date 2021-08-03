N = int(input())
n = list(map(int, str(N)))
a = len(n)

if a % 2 == 0:
    print((int((10**int(a) - 1) / 11)))
else:
    if a == 1:
        print(N)
    else:
        print((int(((100**int(a / 2) - 1) / 11)) + N - 10**int(a - 1) + 1))
