n = int(input())
a = 1
finished = False
while 3 ** a < n:
    b = 1
    while 3 ** a + 5 ** b <= n:
        if 3 ** a + 5 ** b == n:
            print(a, b)
            finished = True
            break
        b += 1
    if finished:break
    a += 1

if not finished: print(-1)
