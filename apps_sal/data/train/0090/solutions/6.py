for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lock = list(map(int, input().split()))
    b = []
    for i in range(n):
        if lock[i] == 0:
            b.append(a[i])
    b.sort()
    b=b[::-1]
    ind = 0
    for i in range(n):
        if lock[i] == 0:
            a[i]=b[ind]
            ind+=1
    a=[str(i) for i in a]
    print(" ".join(a))
