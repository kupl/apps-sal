def L():
    return list(map(int, input().split()))


def I():
    return int(input())


(n, t) = (I(), L())
k = s = i = 2
while i < n:
    if t[i] == t[i - 1] + t[i - 2]:
        s += 1
    else:
        (k, s) = (max(k, s), 2)
    i += 1
print(max(k, s) - int(n == 1))
