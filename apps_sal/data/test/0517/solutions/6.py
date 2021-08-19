(n, d, h) = map(int, input().split())
if d > h * 2 or (h == 1 and d == 1 and (n != 2)):
    print(-1)
else:
    save = 1
    for i in range(2, h + 2):
        print(save, i)
        save = i
    save = 1
    for i in range(h + 2, d + 2):
        print(save, i)
        save = i
    if d - h > 1:
        save = d
    elif d == h:
        save = h
    else:
        save = 1
    for i in range(d + 2, n + 1):
        print(save, i)
