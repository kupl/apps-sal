(n, k) = map(int, input().split())
h = []
ma = 10 ** 9
for i in range(n):
    a = int(input())
    h.append(a)
h.sort()
for i in range(n - k + 1):
    sa = h[k - 1 + i] - h[i]
    if sa < ma:
        ma = sa
print(ma)
