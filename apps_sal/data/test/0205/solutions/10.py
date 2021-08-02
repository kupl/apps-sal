n, b = map(int, input().split())
cnt = {}
i = 2
while i * i <= b:
    while b % i == 0:
        cnt[i] = cnt.setdefault(i, 0) + 1
        b //= i
    i += 1
if b > 1:
    cnt[b] = 1


def get(x):
    ret = 0
    d = x
    while d <= n:
        ret += n // d
        d *= x
    return ret


ans = int(1e30)
for (a, t) in cnt.items():
    ans = min(ans, get(a) // t)
print(ans)
