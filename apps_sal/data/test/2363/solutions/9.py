n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    ans = 0
    while b:
        ans += a // b
        (a, b) = (b, a % b)
    print(ans)
