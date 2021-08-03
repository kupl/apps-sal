n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
x = [0]
for i in range(n):
    x += [v[i]] * t[i] * 2
x += [0]
l = [min(x[i], x[i + 1])for i in range(len(x) - 1)]
for i in range(1, len(l)):
    l[i] = min(l[i], l[i - 1] + 0.5)
for i in range(len(l) - 2, -1, -1):
    l[i] = min(l[i], l[i + 1] + 0.5)
print(sum(0.25 * (l[i] + l[i - 1])for i in range(1, len(l))))
