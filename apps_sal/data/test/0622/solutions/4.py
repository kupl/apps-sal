def f(n, k):
    m = our[n]
    if m // 2 + 1 == k:
        return n
    return f(n - 1, k % (m // 2 + 1))


our = [0, 1]
n, k = map(int, input().split())
while len(our) <= n + 1:
    our.append(our[-1] * 2 + 1)
print(f(n, k))
