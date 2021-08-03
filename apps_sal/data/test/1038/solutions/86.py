a, b = map(int, input().split())
a -= 1


def allx(n):
    ans = 0
    for i in range(40):
        if i == 0:
            if n % 4 == 2 or n % 4 == 1:
                ans += 1
                continue
        c = pow(2, i + 1)
        k = n % c

        if k >= c // 2 and k % 2 == 0:
            ans += pow(2, i)
    return ans


print(allx(b) ^ allx(a))
