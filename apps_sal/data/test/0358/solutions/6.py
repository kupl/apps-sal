def f(a, b):
    t = [1] * (b + 1)
    for i in range(3, int(b ** 0.5) + 1):
        if t[i]:
            t[i * i::2 * i] = [0] * ((b - i * i) // (2 * i) + 1)
    return [i for i in range(3, b + 1, 2) if t[i] and i > a]


(a, b, k) = list(map(int, input().split()))
p = f(a - 1, b)
if 3 > a and b > 1:
    p = [2] + p
if k > len(p):
    print(-1)
elif len(p) == k:
    print(max(p[k - 1] - a + 1, b - p[0] + 1))
else:
    print(max(p[k - 1] - a + 1, b - p[len(p) - k] + 1, max((p[i + k] - p[i] for i in range(len(p) - k)))))
