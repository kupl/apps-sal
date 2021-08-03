n = int(input())


def cal(a):
    return len(str(a))


m = 11
for i in range(1, 6):
    for j in range(1, 10**i + 1):
        if n % j == 0:
            m = min(m, max(cal(j), cal(n // j)))
            # print(m)
print(m)
