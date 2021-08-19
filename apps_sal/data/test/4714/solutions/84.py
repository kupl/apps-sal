(a, b) = [int(x) for x in input().split()]


def check(p):
    p = str(p)
    if p[0] == p[4] and p[1] == p[3]:
        return True
    return False


res = 0
for i in range(a, b + 1):
    if check(i):
        res += 1
print(res)
