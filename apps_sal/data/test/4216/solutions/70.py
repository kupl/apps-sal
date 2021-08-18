n = int(input())


def cal(a):
    return len(str(a))


m = 11
for j in range(1, 10**5 + 1):
    if n % j == 0:
        m = min(m, max(cal(j), cal(n // j)))
print(m)
