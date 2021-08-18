a, b = list(map(int, input().split()))
if b >= a + 10:
    print(0)
else:
    cnt = 1
    for i in range(a + 1, b + 1):
        cnt *= i
        cnt %= 10
    print(cnt)
