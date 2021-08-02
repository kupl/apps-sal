n, m = map(int, input().split())
h = list(map(int, input().split()))
r = []

t = ['W'] * n

for i in range(m):
    a, b = list(map(int, input().split()))
    if h[a - 1] >= h[b - 1]:
        t[b - 1] = 'L'
    if h[a - 1] <= h[b - 1]:
        t[a - 1] = 'L'
print(t.count('W'))
