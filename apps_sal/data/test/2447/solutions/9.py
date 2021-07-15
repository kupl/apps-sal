for _ in range(int(input())):
    A = str(input())
    x = 0
    for i in range(len(A)):
        if A[i] == '1':
            x += 1
    minn = x
    xx = x
    for i in range(len(A)):
        if A[i] == '1':
            xx -= 1
        else:
            xx += 1
        minn = min(minn, xx)
    xx = len(A) - x
    minn = min(minn, len(A) - x)
    for i in range(len(A)):
        if A[i] == '0':
            xx -= 1
        else:
            xx += 1
        minn = min(minn, xx)
    print(minn)
