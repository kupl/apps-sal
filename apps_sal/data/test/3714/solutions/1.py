def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
a = list(map(int, input().split()))
if sorted(a) != [i + 1 for i in range(n)]:
    print(-1)
else:
    ans = 1
    used = [0 for i in range(n)]
    for i in range(n):
        if used[i] == 0:
            j = i
            am = 0
            while used[j] == 0:
                am += 1
                used[j] = 1
                j = a[j] - 1
            if am % 2:
                ans = lcm(ans, am)
            else:
                ans = lcm(ans, am // 2)
    print(ans)
