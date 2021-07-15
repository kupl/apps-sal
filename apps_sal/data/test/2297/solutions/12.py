Q = int(input())

def getsum(N):
    A = (N+1)//2
    r1 = -A + A*(A+1)
    B = N // 2
    r2 = B*(B+1)
    return -r1 + r2

while Q != 0:
    L, R = list(map(int, input().split()))
    print(getsum(R) - getsum(L-1))
    Q -= 1
    

