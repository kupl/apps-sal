for i in range(int(input())):
    k = int(input())
    BIG = input()
    max_ = 0
    calcer = 0
    f = 0
    for j in range(k):
        if BIG[j] == 'A':
            f = 1
            max_ = max(calcer, max_)
            calcer = 0
        if BIG[j] == 'P' and f:
            calcer += 1
    max_ = max(max_, calcer)
    print(max_)
