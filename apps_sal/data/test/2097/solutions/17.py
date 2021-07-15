for t in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    zero = 0
    ssum = 0
    for i in l:
        ssum += i
        if (not i):
            zero += 1
    res = zero
    if (ssum + zero == 0):
        res += 1
    print(res)
