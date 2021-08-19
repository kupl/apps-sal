(n, v) = list(map(int, input().split()))
count = 0
res = []


def f(a):
    for k in a:
        if v > k:
            return True
    return False


for i in range(n):
    a = list(map(int, input().split(' ')))
    a.pop(0)
    if f(a):
        count += 1
        res.append(i + 1)
print(count)
print(' '.join((str(e) for e in res)))
