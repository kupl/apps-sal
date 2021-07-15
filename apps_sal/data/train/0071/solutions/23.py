for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ans = 0
    a = 0
    b = 0
    for elem in ar:
        if elem < 0:
            if b > -elem:
                b += elem
                a += elem
            else:
                ans += abs(elem) - b
                b = 0
                a += abs(elem) - b
        else:
            b += elem
    print(ans)
