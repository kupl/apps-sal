t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0
    while n >= 1:
        cnt += n
        n = n // 2
    print(cnt)






