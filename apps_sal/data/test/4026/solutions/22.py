t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    m = int(l[1])
    l = []
    col = dict()
    row = dict()
    found = 0
    done = 0
    for i in range(n):
        lo = input().split()
        a = int(lo[0])
        b = int(lo[1])
        lo = input().split()
        c = int(lo[0])
        d = int(lo[1])
        if b == c:
            found = 1
    if found == 1 and m % 2 == 0:
        print('YES')
    else:
        print('NO')
