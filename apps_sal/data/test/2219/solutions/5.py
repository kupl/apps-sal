n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    ans = 0
    while a > 0:
        if a % b == 0:
            a //= b
            ans += 1
        else:
            ans += a - a // b * b
            a = a // b * b
    print(int(ans))
