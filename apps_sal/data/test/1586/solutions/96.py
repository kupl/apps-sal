n = int(input())
if n % 2 == 1:
    print(0)
else:
    ans = 0
    cnt = 1
    while n >= (5**cnt):
        ans += n // (5**cnt) // 2
        cnt += 1
    print(ans)
