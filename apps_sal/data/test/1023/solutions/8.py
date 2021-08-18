from bisect import bisect_left

n, m, ta, tb, k = list(map(int, input().split()))
a = [int(x) + ta for x in input().split()]
b = [int(x) for x in input().split()]
if k >= len(a) or k >= len(b):
    print(-1)
    raise SystemExit(0)


def find_ge(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return i
    return None


ans = 0
for i in range(k + 1):
    t = a[i]
    j = find_ge(b, t)
    if j is None:
        print(-1)
        raise SystemExit(0)
    j += k - i
    if j >= len(b):
        print(-1)
        raise SystemExit(0)
    ans = max(ans, b[j] + tb)
print(ans)
