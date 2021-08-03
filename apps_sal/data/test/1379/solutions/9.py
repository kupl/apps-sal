from collections import Counter, defaultdict, deque
def read(): return list(map(int, input().split()))


def solve(a, d, df):
    cnt = 1
    res = [0] * n
    Q = deque([(a[0], cnt)])
    res[df[a[0]]] = 1
    for i in range(1, n):
        if a[i] > Q[0][0] + d:
            val, day = Q.popleft()
            res[df[a[i]]] = day
            Q.append((a[i], day))
        else:
            cnt += 1
            res[df[a[i]]] = cnt
            Q.append((a[i], cnt))
    print(cnt)
    print(' '.join(map(str, res)))


n, m, d = read()
a = read()
df = {v: i for i, v in enumerate(a)}
a.sort()
solve(a, d, df)
