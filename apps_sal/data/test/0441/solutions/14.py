import re


def R():
    return list(map(int, input().split()))


(n, a, b) = R()
s = input()
s0 = a + b
for t in re.findall('\\.+', s):
    t = len(t)
    if t % 2:
        if a > b:
            a -= 1
        else:
            b -= 1
        t -= 1
    a -= t / 2
    b -= t / 2
print(int(s0 - max(0, a) - max(0, b)))
