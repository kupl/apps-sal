import sys
n, m = list(map(int, input().split()))

le = 2 ** 30

for i in range(m):
    l, r = list(map(int, input().split()))
    le = min(r - l + 1, le)


a = (list(range(0, le)) * ((n + le - 1) // le))[:n]
res = " ".join(map(str, a))
print(le)
print(res)
