for _ in range(int(input())):
    n = int(input())
    a = [int(s) for s in input().split()]

    a = sorted(a)[::-1]
    m = 0
    for i in range(1, n+1):
        m = max(m, min(i, a[i-1]))

    print(m)
