(n, k, x) = list(map(int, input().split()))
s = list(map(int, input().split()))


def fl(x, e, c):
    s = x[:e]
    s.append(c)
    s += x[e:]
    for j in range(55):
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2]:
                if i < len(s) - 3:
                    if s[i] == s[i + 3]:
                        del s[i]
                del s[i]
                del s[i]
                del s[i]
                break
    return len(s)


m = 0
for i in range(n):
    m = max(m, n - fl(s, i, x))
print(m)
