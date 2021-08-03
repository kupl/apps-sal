for _ in range(int(input())):
    n = int(input())
    mxa = mxb = 0
    for i in sorted(map(int, input().split())):
        if i == mxa:
            mxa += 1
        elif i == mxb:
            mxb += 1
    print(mxa + mxb)
