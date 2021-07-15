t = int(input())
for _ in range(t):
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    white = set()
    if not T%2 and T//2 in a:
        halfcount = 0
        for i in range(len(a)):
            if a[i] == T//2:
                if halfcount % 2:
                    a[i] = 1
                else:
                    a[i] = 0
                halfcount += 1
            else:
                if T-a[i] in white:
                    a[i] = 1
                else:
                    white.add(a[i])
                    a[i] = 0
    else:
        for i in range(len(a)):
            if T-a[i] in white:
                a[i] = 1
            else:
                white.add(a[i])
                a[i] = 0
    print(*a)
