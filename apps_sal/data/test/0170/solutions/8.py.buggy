import sys

n = int(input())
d1 = list(map(int, input().split(" ")))
d2 = list(map(int, input().split(" ")))
k1 = d1[0]
k2 = d2[0]
d1.remove(d1[0])
d2.remove(d2[0])

moves = 0

while True:
    if moves > 500000:
        print(-1)
        return
    a = d1[0]
    d1.remove(d1[0])
    b = d2[0]
    d2.remove(d2[0])
    if a > b:
        moves += 1
        d1.append(b)
        d1.append(a)
        if len(d2) == 0:
            print(str(moves) + " 1")
            return
    if b > a:
        moves += 1
        d2.append(a)
        d2.append(b)
        if len(d1) == 0:
            print(str(moves) + " 2")
            return
