k = int(input())


def S(num):
    s = sum(map(int, list(str(num))))
    return num / s


ten = 0
now = 1
for _ in range(k):
    print(now)
    if S(now + 10**ten) > S(now + 10**(ten + 1)):
        ten += 1
    now += 10**ten
