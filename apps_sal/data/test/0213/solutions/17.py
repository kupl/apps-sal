(n, m) = map(int, input().split())
l = set()
s = {i for i in range(1, 101)}
b = False
for i in range(m):
    (k, f) = map(int, input().split())
    if k == n:
        print(f)
        b = True
        break
    j = 1
    if f == 1:
        l = {i for i in range(k, 101)}
    else:
        while j <= (k - j) // (f - 1):
            if (k - j) % (f - 1) == 0:
                l.add((k - j) // (f - 1))
                j += f - 1
            else:
                j += 1
    s &= l
    l.clear()
a = -1
if b == False:
    t = True
    for j in s:
        if a == -1:
            a = (n - 1) // j
        elif (n - 1) // j != a:
            print(-1)
            t = False
            break
    if t == True:
        print(a + 1)
