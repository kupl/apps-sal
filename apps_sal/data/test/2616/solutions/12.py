for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    x = 1
    for i in range(len(A) - 2, - 1, -1):
        if A[i] == 1:
            x += 1
        else:
            if x % 2 == 0:
                x = 1
    if x % 2 == 1:
        print('First')
    else:
        print('Second')
