def f(c):
    return ord(c) - ord('a')


def dalp(x, y):
    return min(abs(x - y), abs(x + 26 - y), abs(y + 26 - x))


def dist(i, j):
    return min(abs(i - j), abs(i + n - j), abs(j + n - i))


def read():
    return list(map(int, input().split()))


(n, p) = read()
a = [f(i) for i in input()]
(pr, sf) = ([], [])
cnt = 0
for i in range(n // 2):
    if a[i] != a[n - i - 1]:
        cnt += dalp(a[i], a[n - i - 1])
        pr.append(i)
        sf.append(n - i - 1)
if pr:
    p -= 1
    d1 = dist(pr[0], pr[-1])
    d2 = min(dist(p, pr[0]), dist(p, pr[-1]), dist(p, sf[0]), dist(p, sf[-1]))
    cnt += d1 + d2
print(cnt)
