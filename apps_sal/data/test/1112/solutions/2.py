3

def readln(): return tuple(map(int, input().split()))

s = [list(readln()) for _ in range(3)]
for x in range(1, 10**5 + 1):
    ss = x + s[0][1] + s[0][2]
    y = ss - s[1][0] - s[1][2]
    z = ss - s[2][0] - s[2][1]
    if x + y + z == ss:
        s[0][0] = x
        s[1][1] = y
        s[2][2] = z
        for _ in s:
            print(*tuple(_))

