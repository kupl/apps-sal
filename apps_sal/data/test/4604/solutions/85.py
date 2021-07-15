from collections import Counter

N,*A = map(int, open(0).read().split())
ac = Counter(A)
if N % 2 == 0:
    for i in range(1,N,2):
        if ac[i] != 2:
            print(0)
            break
    else:
        print(pow(2,N//2,1000000007))
else:
    if ac[0] != 1:
        print(0)
    else:
        for i in range(2,N,2):
            if ac[i] != 2:
                print(0)
                break
        else:
            print(pow(2,N//2,1000000007))
