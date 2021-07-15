T = int(input())

for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]
    even = [el for el in A if el % 2 == 0]
    odd = [el for el in A if el % 2 == 1]
    sA = sorted(A)
    v = 0
    for i in range(len(A)-1):
        if sA[i+1] - sA[i] == 1:
            v += 1
    if len(even) % 2 == 0 and len(odd) % 2 == 0:
        print('YES')
    else:
        if v > 0:
            print('YES')
        else:
            print('NO')

