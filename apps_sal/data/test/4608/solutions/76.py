n = int(input())
a = [0] + [int(input()) for i in range(n)]
cnt = 1
next_a = a[1]
if a[1] == 2:
    print(cnt)
else:
    while cnt <= 10 ** 5:
        next_a = a[next_a]
        cnt += 1
        if next_a == 2:
            break
    if cnt <= 10 ** 5:
        print(cnt)
    else:
        print(-1)
