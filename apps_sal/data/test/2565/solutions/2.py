from queue import Queue

def rn():
    a = int(input())
    return a


def rl():
    a = list(map(int, input().split()))
    return a

for _ in range(rn()):
    [x1,y1,z1] = rl()
    [x2, y2, z2] = rl()
    ans = 0
    h1 = min(z1,y2)
    ans += 2*h1
    z1 -= h1
    y2 -= h1
    rem = x1+z1
    h2 = min(rem,z2)
    z2 -= h2
    ans -= 2*z2
    print(ans)



