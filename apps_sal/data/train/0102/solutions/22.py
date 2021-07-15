for __ in range(int(input())):
    n = int(input())
    x = n
    num = 0
    while x >= 10:
        x //= 10
        num += 1
    ans = num * 9
    ans += (n // int('1' * (num + 1)))
    print(ans)
