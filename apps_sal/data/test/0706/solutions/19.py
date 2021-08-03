
(a, b, n, x) = map(int, input().split(" "))

xp = pow(a, n % 1000000006, 1000000007)

ans = (xp * x) % 1000000007

if (a == 1):

    ans = ans + n * b

else:

    tmp = (xp - 1) * pow(a - 1, 1000000005, 1000000007) * b

    tmp = tmp % 1000000007

    ans = ans + tmp

ans = ans % 1000000007

print(ans)
