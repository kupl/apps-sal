n = int(input())
a = []


def mem(kek):
    return (int(kek[0]) * 10 + int(kek[1])) * 60 + int(kek[3]) * 10 + int(kek[4])


def lol(kek):
    h = str(kek // 60)
    m = str(kek % 60)
    ans = ""
    if (len(h) < 2):
        ans += "0"
    ans += h
    ans += ":"
    if (len(m) < 2):
        ans += "0"
    ans += m
    return ans


delt = 60 * 24
for i in range(n):
    st = input()
    a.append(mem(st))
    a.append(mem(st) + delt)
    a.append(mem(st) + 2 * delt)

a = sorted(a)
ans = 0
for i in range(1, len(a)):
    ans = max(ans, a[i] - a[i - 1] - 1)
print(lol(ans))
