from sys import stdin
q = int(stdin.readline().strip())
for i in range(q):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    x = s.index(1)
    y = 1
    t = True
    for i in range(n):
        if s[x] != y:
            t = False
            break
        x = (x + 1) % n
        y += 1
    t1 = True
    x = s.index(1)
    y = 1
    for i in range(n):

        if s[x] != y:
            t1 = False
            break
        x = (x - 1) % n
        y += 1
    if t or t1:
        print("YES")
    else:
        print("NO")
