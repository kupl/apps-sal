(n, k) = list(map(int, input().split()))
(r, s, p) = list(map(int, input().split()))
T = input()
record = [False for _ in range(n)]
ans = 0


def win(t):
    if t == 'r':
        return p
    elif t == 's':
        return r
    else:
        return s


for (i, t) in enumerate(T):
    if i < k:
        ans += win(t)
        record[i] = t
    else:
        f = record[i - k]
        if f:
            if f == t:
                continue
            else:
                ans += win(t)
                record[i] = t
        else:
            ans += win(t)
            record[i] = t
print(ans)
