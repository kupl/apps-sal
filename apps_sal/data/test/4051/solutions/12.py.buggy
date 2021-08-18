n = int(input())
r = list(map(int, input().split(' ')))
s = []


def ok():
    prev = r[0]
    for ra in r[1:]:
        if abs(ra - prev) >= 2:
            return False
        prev = ra
    return True


while len(r):
    if not ok():
        print('NO')
        return

    maxi = 0
    for i in range(len(r)):
        if r[i] > r[maxi]:
            maxi = i
    r.pop(maxi)

print('YES')
