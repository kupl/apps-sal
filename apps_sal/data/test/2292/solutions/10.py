t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    paira = []
    for i in range((n + 1) // 2):
        paira.append(tuple(sorted([a[i], a[~i]])))

    pairb = []
    for i in range((n + 1) // 2):
        pairb.append(tuple(sorted([b[i], b[~i]])))

    paira.sort()
    pairb.sort()

    if paira == pairb:
        print("Yes")
    else:
        print("No")
