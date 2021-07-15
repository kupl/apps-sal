ALL = []
cnt = 0
import math
def decide_sosuu(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True
for i in range(1,int((10**5)/2+2)):
    if decide_sosuu(i):
        if decide_sosuu((i*2)-1):
            cnt += 1
            ALL.append(cnt)
        else:
            ALL.append(cnt)
    else:
        ALL.append(cnt)
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    if l == 1:
        print(ALL[int(r/2)])
    else:
        print(ALL[int(r/2)] -ALL[int(l/2)-1])
