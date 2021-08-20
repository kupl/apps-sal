(D, P) = map(int, input().split())
ans = 0.0


def func(i):
    t = 0
    while i < P:
        i *= 2
        t += 1
    return t


for i in range(1, D + 1):
    ans += float(1 / D) * float((1 / 2) ** func(i))
print(ans)
