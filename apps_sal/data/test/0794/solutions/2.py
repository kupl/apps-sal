n = int(input())
l1 = list(map(int, input().split()))
if l1.count(l1[0]) != 2 * n:
    l1.sort()
    print(' '.join((str(x) for x in l1)))
else:
    print(-1)
