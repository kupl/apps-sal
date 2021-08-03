n, m, k = list(map(int, input().split()))
ps = list(map(int, input().split()))
xs = []
for _ in range(n):
    xs.append(list(map(int, input().split())))


def get(x):
    i = ps.index(x)
    ps[1:i + 1] = ps[0:i]
    ps[0] = x
    return i + 1


print(sum([sum(map(get, ys)) for ys in xs]))
