def M(): return map(int, input().split())
def L(): return list(map(int, input().split()))
def I(): return int(input())


n, k = M()
t = [0] + L()
a, b = list(range(n + 1)), list(range(n + 1))
for i in range(n, 1, -1):
    if t[i] >= t[i - 1]:
        a[i - 1] = a[i]
    if t[i] <= t[i - 1]:
        b[i - 1] = b[i]
p = ['No'] * k
for i in range(k):
    x, y = M()
    if b[a[x]] >= y:
        p[i] = 'Yes'
print('\n'.join(p))
