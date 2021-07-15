for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a == sorted(a):
        print('Yes')
    else:
        ch0 = 0
        ch1 = 0
        for i in b:
            if i == 0:
                ch0 += 1
            else:
                ch1 += 1
        if ch1 == 0 or ch0 == 0:
            print('No')
        else:
            print('Yes')
