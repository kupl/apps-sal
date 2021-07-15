from queue import Queue

def rn():
    a = int(input())
    return a


def rl():
    a = list(map(int, input().split()))
    return a

for _ in range(rn()):
    [a,k] = rl()
    ans = 0
    if k<=a:
        if (k+a)%2 == 0:
            ans = 0
        else:
            ans = 1
    else:
        ans = (k-a)
        a = k
        if (k+a)%2 != 0:
            ans += 1
    print(ans)


