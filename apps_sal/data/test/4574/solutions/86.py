import collections
N = int(input())
A = sorted(collections.Counter((int(T) for T in input().split())).most_common(), reverse=True)
Flag = False
LS = 0
SS = 0
for T in range(0, len(A)):
    if LS == 0 and A[T][1] >= 4:
        Sq = A[T][0] ** 2
        Flag = True
        break
    if A[T][1] >= 2:
        if LS == 0:
            LS = A[T][0]
        else:
            SS = A[T][0]
            Sq = LS * SS
            Flag = True
            break
if Flag:
    print(Sq)
else:
    print(0)
