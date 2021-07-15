from sys import stdin
from sys import setrecursionlimit as SRL; SRL(10**7)
rd = stdin.readline
rrd = lambda: list(map(int, rd().strip().split()))

s = str(rd().strip())

t = str(rd().strip())
s = '0' + s

canl = [0] * (len(s) + 10)
canr = [0] * (len(s) + 10)

j = 0
for i,v in enumerate(s):

    if j<len(t) and v == t[j]:
        j += 1
    canl[i] = j

j = len(t) - 1

for i in range(len(s)-1,-1,-1):
    if j>=0 and s[i] == t[j]:
        j -= 1
    canr[i] = len(t)-j-1


def check(x):
    if x > len(s):
        return False

    for i in range(1,len(s) - x+1):
        l = i - 1
        r = i + x

        if canl[l] + canr[r] >= len(t):

            return True

    return False


l = 0
r = len(s)


while l<r:
    mid = (l+r)//2
    if check(mid):
        l = mid + 1
    else:
        r = mid


print(r-1)






