from math import ceil
import sys
input = sys.stdin.readline
n, a, b, k = map(int, input().split())
arr = [int(i) for i in input().split()]
if a <= b:
    req = []
    sm = 0
    sm += sum(i <= a for i in arr)
    arr = [i for i in arr if i > a]
    tot = a + b
    chance = k
    for x in arr:
        now = x % tot
        if now > 0 and now <= a:
            sm += 1
        else:
            curr = now
            if curr == 0:
                curr = tot
            curr -= a
            req.append(ceil(curr / a))
    req.sort()
   # print(req)
    for x in req:
        if x <= chance:
            sm += 1
            chance -= x
        else:
            break
    print(sm)

else:
    sm = 0
    sm += sum(i <= a for i in arr)
    arr = [i for i in arr if i > a]
    tot = a + b
    chance = k
    for x in arr:
        now = x % tot
        if now > 0 and now <= a:
            sm += 1
        else:
            if chance:
                sm += 1
                chance -= 1
    print(sm)
