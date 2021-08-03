def invert(x):
    if x == 1:
        return 0
    else:
        return 1


n, k = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
t = list(map(int, input().strip().split()))

base = sum([a * b for a, b in zip(a, t)])

t = list(map(invert, t))
t = [a * b for a, b in zip(a, t)]
for i in range(1, len(t)):
    t[i] += t[i - 1]

rslt = t[k - 1]
for i in range(1, n - k + 1):
    rslt = max(rslt, t[i + k - 1] - t[i - 1])

print(rslt + base)
