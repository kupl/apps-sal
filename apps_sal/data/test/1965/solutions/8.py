T = int(input())
for _ in range(T):
    N, X = list(map(int, input().split()))
    A = [int(a) for a in input().split()]
    if A.count(X) == N:
        print(0)
    elif sum(A) == N * X or A.count(X) > 0:
        print(1)
    else:
        print(2)



