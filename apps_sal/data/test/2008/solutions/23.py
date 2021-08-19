def in_int():
    return int(input())


def in_list():
    return [int(x) for x in input().split()]


n = int(input())
ns = []
ans = 0
for i in range(n):
    (x, y) = in_list()
    ns.append(x - y)
    ans += -x + y * n
ns.sort(reverse=True)
for i in range(n):
    c = ns[i]
    ans += c * (i + 1)
print(ans)
