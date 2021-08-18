n, p = map(int, input().split())
a = list(map(int, input().split()))


def calc(x):
    nonlocal n, p, a
    o = [0] * (n + 1)
    for i in a:
        o[max(0, min(n, i - x))] += 1
    s = 0
    ans = 1
    for i in range(n):
        s += o[i]
        if s <= 0:
            return 0
        ans = ans * s % p
        s -= 1
    return ans


ans = []
for x in range(4020):
    if calc(x):
        ans.append(x)
print(len(ans))
print(*ans)
