n = int(input())
if n % 2 != 0:
    print(0)
else:
    cnt = 0
    n = n // 2
    while n > 0:
        cnt = cnt + n // 5
        n = n // 5
    print(cnt)
