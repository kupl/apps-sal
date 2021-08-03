from collections import defaultdict
n = int(input())
s = input()


def check(l):
    d = defaultdict(lambda: -1)
    for i in range(n - l + 1):
        if d[s[i:i + l]] != -1:
            if d[s[i:i + l]] + l <= i:
                return True
        else:
            d[s[i:i + l]] = i
    return False


ok = 0
ng = len(s)

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
