n, k = map(int, input().split())
h = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + h[i]
x = 0
y = s[-1]
for i in range(n - k + 1):
    if s[i + k] - s[i] < y:
        x = i
        y = s[i + k] - s[i]
print(x + 1)
