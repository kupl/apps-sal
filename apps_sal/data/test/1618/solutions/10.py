n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = {}
t = []
for i in range(m):
    (w, h) = list(map(int, input().split()))
    x = max(a[0], a[w - 1])
    t.append(x)
    a[0] = x + h
    a[w - 1] = x + h
for i in range(m):
    print(t[i])
