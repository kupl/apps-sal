n, k = map(int, input().split())
num = [0] * k
ans = 0


def njo(arg, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return njo((arg**2) % 1000000007, n // 2)
    else:
        return arg * njo((arg**2) % 1000000007, n // 2)


for i in range(k):
    test = k - i
    num[test - 1] = njo(k // test, n)
    mul = test * 2
    while mul <= k:
        num[test - 1] -= num[mul - 1]
        mul += test

    ans += num[test - 1] * test

while ans < 0:
    ans += 1000000007
print(str(ans % 1000000007))
