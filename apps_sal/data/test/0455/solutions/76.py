n = int(input())
place = [tuple(map(int, input().split())) for _ in range(n)]
m = 0
def bitlist(x):
    ret = [0] * 31
    for i in reversed(range(31)):
        if x > 0:
            x -= 1 << i
            ret[i] = 1
        else:
            x += 1 << i
            ret[i] = -1
    return ret
pre = (place[0][0] + place[0][1] + 1) % 2
for x, y in place:
    if (x + y + 1) % 2 != pre:
        print(-1)
        return
print(31 + pre)
if pre:
    print(1, end = ' ')
for i in reversed(range(31)):
    print(1 << i, end = ' ')
print()
for x, y in place:
    u = x + y
    v = x - y
    if pre:
        u -= 1
        v -= 1
    ubit = bitlist(u)
    vbit = bitlist(v)
    if pre:
        print('R', end = '')
    for i in reversed(range(31)):
        if ubit[i] == 1 and vbit[i] == 1:
            print('R', end = '')
        elif ubit[i] == 1 and vbit[i] == -1:
            print('U', end = '')
        elif ubit[i] == -1 and vbit[i] == -1:
            print('L', end = '')
        else:
            print('D', end = '')
    print()

