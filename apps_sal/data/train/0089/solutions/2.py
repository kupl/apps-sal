import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n < 3:
        print(1)
        continue
    old = [0]
    h = 1
    nind = prev = cum = 0
    for i in range(1,n):
        if a[i] < prev:
            nind += 1
            if nind >= len(old):
                old = [0] * cum
                nind = cum = 0
                h += 1
        prev = a[i]
        old[nind] += 1
        cum += 1
    print(h)
