n = int(input())
b = [int(i) for i in input().split()]
_b = []

if n == 1:
    print(0)
    return


def check(diff):
    cnt = 0
    for i in range(2, n):
        if b[i] - _b[-1] == diff:
            _b.append(b[i])
        elif b[i] - _b[-1] - 1 == diff:
            _b.append(b[i] - 1)
            cnt += 1
        elif b[i] - _b[-1] + 1 == diff:
            _b.append(b[i] + 1)
            cnt += 1
        else:
            return -1
    return cnt


ans = n + 1
d = [-1, 0, 1]
for d1 in d:
    for d2 in d:
        _b = [b[0] + d1, b[1] + d2]
        cur = check(_b[1] - _b[0])
        if cur != -1:
            ans = min(ans, cur + abs(d1) + abs(d2))
print(ans if ans < n + 1 else -1)
