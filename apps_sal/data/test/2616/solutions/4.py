for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.reverse()
    ans = 0
    for elem in ar:
        if elem == 1:
            ans += 1
        else:
            ans = 1
    if ans % 2 != 0:
        print('First')
    else:
        print('Second')
