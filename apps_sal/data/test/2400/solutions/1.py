T = int(input())
for i in range(T):
    N = int(input())
    ps = list(map(int, input().split()))
    M = int(input())
    qs = list(map(int, input().split()))

    peven = 0
    podd = 0
    for i in ps:
        if i % 2 == 0:
            peven += 1
        else:
            podd += 1

    qeven = 0
    qodd = 0
    for i in qs:
        if i % 2 == 0:
            qeven += 1
        else:
            qodd += 1

    print(qeven * peven + qodd * podd)
