def read(): return [int(i) for i in input().split()]


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    ans = 0
    if n % 2:
        ans += 1
        n -= 3
    ans += n // 2
    print(ans)
