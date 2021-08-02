T = int(input())
for t in range(T):
    a = int(input())
    cnt = 0
    while a != 0:
        if a % 2 == 1:
            cnt += 1
        a >>= 1
    print(1 << cnt)
