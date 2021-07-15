import math

def checksum(n):
    return sum([int(x) for x in str(n)])

for _ in range(int(input())):
    n,s = [int(p) for p in input().split()]
    moves = 0
    if checksum(n)<=s:
        print(0)
    else:
        pow = 10
        while True:
            # print(n)
            closest = pow*((n+pow-1)//pow)
            # print(closest)
            moves += (closest-n)
            n = closest
            if checksum(n)<=s:
                break
            pow*=10
        print(moves)
