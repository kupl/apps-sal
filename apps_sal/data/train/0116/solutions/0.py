for nt in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)
    e = l[0]
    for i in range(1, n):
        e = e ^ l[i]
    if s == 2 * e:
        print(0)
        print()
    else:
        print(2)
        print(e, s + e)
