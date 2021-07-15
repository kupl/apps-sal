one = []
for i in range(17):
    one.append(0)


def code():
    i = 1
    j = 0
    k = 0
    one[0] = 0
    for i in range(1, 17):
        one[i] = one[i-1]*10+1
    n = int(input())
    print(df(n, 16))


def df(n, i):
    k = int(n/one[i])
    n %= one[i]
    if n == 0:
        return k*i
    else:
        return k*i+min(i+df(one[i]-n, i-1), df(n, i-1))


code()

