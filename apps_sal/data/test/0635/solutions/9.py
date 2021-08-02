def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n, s = mi()
a = li()
b = li()
s -= 1

ok = 1
if s == 0:
    ok = 1
elif a[0] == 0:
    ok = 0
elif a[s]:
    ok = 1
elif b[s] == 0:
    ok = 0
else:
    ok = any(a[i] == 1 and b[i] == 1 for i in range(s + 1, n))
print('YES' if ok else 'NO')
