for i in range(int(input())):
    x = int(input())
    #n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == A[-1]:
        print(len(A))
    else:
        print(1)
