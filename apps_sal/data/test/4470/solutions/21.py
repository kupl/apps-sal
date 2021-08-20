q = int(input())
for t in range(q):
    n = int(input())
    ans = 0
    while n % 5 == 0:
        n //= 5
        ans += 3
    while n % 3 == 0:
        n //= 3
        ans += 2
    while n % 2 == 0:
        n //= 2
        ans += 1
    if n == 1:
        print(ans)
    else:
        print(-1)
