
T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    tmp1 = 0
    tmp2 = 0

    for i in range(len(a)):
        if i % 2 == 0:
            tmp1 += a[i]
        else:
            tmp2 += a[i]

    if N % 2 == 0:
        if tmp1 != tmp2:
            print ("First")
        else:
            print ("Second")
    else:
        print ("Second")
