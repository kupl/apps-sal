t = int(input())
while t:
    t -= 1
    n, x = list(map(int, input().split()))
    ans = 1
    total = 2
    if n <= 2:
        print(1)
        continue
    while True:
        total += x
        ans += 1
        if total >= n:
            print(ans)
            break
