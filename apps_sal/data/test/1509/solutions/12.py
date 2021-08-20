def in_int():
    return int(input())


def in_list():
    return [int(x) for x in input().split()]


n = in_int()
ns = in_list()
ans = 0
for i in range(n - 1):
    (a, b) = (ns[i], ns[i + 1])
    if a > b:
        ans += (a - b) * (n - a + 1)
    else:
        ans += a * (b - a)
a = ns[-1]
ans += a * (n - a + 1)
print(ans)
