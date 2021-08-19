n = int(input())
cnt = 0
i = 1
x = 10
if n % 2 == 1:
    print(0)
else:
    while x <= n:
        cnt += n // x
        x *= 5
    print(cnt)
