N = int(input())
XN = list(map(int,input().split()))

def answer(N,XN):
    a = min(XN)
    b = max(XN)
    min_distance = float('inf')
    for i in range(a,b+1):
        distance = 0
        for j in XN:
            distance += (i-j) ** 2
        min_distance = min(distance,min_distance)
    print(min_distance)

answer(N,XN)
