def sinsuuton(X, n):
    if (int(X / n)):
        return sinsuuton(int(X / n), n) + str(X % n)
    return str(X % n)


def sinsuutoo10(X, n):
    return sum([X[-i - 1] * n**i for i in range(len(X))])


n = int(input())
ans = float("inf")
for i in range(n + 1):
    t = i
    now = 0
    t6 = sinsuuton(t, 6)
    now += sum([int(i) for i in t6])
    t = n - i
    t9 = sinsuuton(t, 9)
    now += sum([int(i) for i in t9])
    ans = min(ans, now)

print(ans)
