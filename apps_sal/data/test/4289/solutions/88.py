n = int(input())
(t, a) = map(int, input().split())
h = list(map(int, input().split()))
b = 10 ** 9
for i in range(n):
    c = abs(a - (t - h[i] * 0.006))
    if c < b:
        b = c
        d = i
print(d + 1)
