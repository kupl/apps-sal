from itertools import accumulate


def LI():
    return list(map(int, input().split()))


Q = int(input())
n = 10**5
sosu = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    sosu.difference_update(range(i*2, n+1, i))
xlist = [0]*(10**5+1)
for i in range(1, 10**5+1, 2):
    if i in sosu:
        if (i+1)//2 in sosu:
            xlist[i] = 1
Xsum = list(accumulate(xlist))
for _ in range(Q):
    L, R = LI()
    ans = Xsum[R]-Xsum[L-1]
    print(ans)
