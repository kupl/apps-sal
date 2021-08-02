target, limit = list(map(int, input().split()))


def lowbit(x):
    return x & (x ^ (x - 1))


ans = []
for i in range(limit, 0, -1):
    x = lowbit(i)
    if x <= target:
        ans.append(i)
        target -= x

if target:
    print(-1)
else:
    print(len(ans))
    print(" ".join(map(str, ans)))
