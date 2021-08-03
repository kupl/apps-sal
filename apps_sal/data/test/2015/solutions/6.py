for q in range(int(input())):
    n, m, k = sorted(list(map(int, input().split())))
    if k > n + m + 1:
        print('No')
    else:
        print('Yes')
