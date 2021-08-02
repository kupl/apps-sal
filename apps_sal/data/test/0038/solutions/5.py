def track(tr):
    res = [l - tr[-1] + tr[0]]
    for i in range(1, n):
        res.append(tr[i] - tr[i - 1])
    return res


def equals(l1, l2):
    for i in range(n):
        res = True
        for k in range(n):
            res = res and l1[k] == l2[(k + i) % n]
        if res:
            return True
    return False


n, l = list(map(int, input().split()))
a = track(list(map(int, input().split())))
b = track(list(map(int, input().split())))
if equals(a, b):
    print("YES")
else:
    print("NO")
