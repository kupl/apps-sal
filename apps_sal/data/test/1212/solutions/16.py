__author__ = 'asmn'
(n, k) = tuple(map(int, input().split()))
h = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    h[i] += h[i - 1]
s = [h[i] - h[i - k] for i in range(k, n + 1)]
print(s.index(min(s)) + 1)
