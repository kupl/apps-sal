n, m = int(input()), 10 ** 5
a = [list(map(int, input().split())) for i in range(n)]
p, v = [0 for i in range(m)], [0 for i in range(m)]
for i in range(2, m):
    if not v[i]:
        p[0] += 1
        p[p[0]] = i
    for j in range(1, p[0] + 1):
        if i * p[j] >= m:
            break
        v[i * p[j]] = 1
        if i % p[j] == 0:
            break


def ok(x):
    nonlocal a
    for i in a:
        if i[0] % x > 0 and i[1] % x > 0:
            return False
    return True


def judge(x):
    nonlocal p
    for i in p[1:p[0] + 1]:
        if x % i == 0:
            if ok(i):
                print(i)
                return True
            while x % i == 0:
                x //= i
    if x != 1:
        if ok(x):
            print(x)
            return True
    return False


if judge(a[0][0]):
    return
if judge(a[0][1]):
    return
print(-1)
