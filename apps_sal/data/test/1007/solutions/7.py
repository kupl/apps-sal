(k, p) = map(int, input().split())


def zcy(n):
    ans = str(n) + str(n)[::-1]
    return int(ans)


ans = 0
for i in range(1, k + 1):
    ans = (ans + zcy(i)) % p
print(ans)
