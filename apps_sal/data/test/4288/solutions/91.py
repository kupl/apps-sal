def solve(A, B, C):
    if A == B or A == C:
        if A == B and B == C:
            print('No')
        else:
            print('Yes')
    elif B == C:
        print('Yes')
    else:
        print('No')


(a, b, c) = map(int, input().split())
solve(a, b, c)
