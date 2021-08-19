(A, B, C) = list(map(int, input().split()))
D = [A, B, C]
D.sort()
if D.count(A) == 2:
    print('Yes')
elif D.count(A) == 1:
    if B == C:
        print('Yes')
    else:
        print('No')
elif D.count(A) == 3:
    print('No')
