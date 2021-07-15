tests = int(input())
for test in range(tests):
    n = int(input())
    a = [int(i) for i in input().split()]
    w = [False] * n
    w[n - 1] = True
    for i in range(n - 2, -1, -1):
        if a[i] == 1:
            w[i] = not w[i + 1]
        else:
            w[i] = True
    if w[0]:
        print('First')
    else:
        print('Second')

