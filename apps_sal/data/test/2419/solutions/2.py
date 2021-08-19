def rint():
    return int(input())


def rints():
    return list(map(int, input().split()))


t = rint()
for _ in range(t):
    (a, b) = sorted(rints())
    mn = b - a if a % 2 == b % 2 else b - a + 2
    for i in range(10 ** 6):
        s = i * (i + 1) // 2
        if s >= b - a and (s - (b - a)) % 2 == 0:
            print(i)
            break
