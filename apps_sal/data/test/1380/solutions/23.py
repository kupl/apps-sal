n, k = map(int, input().split())
l = [int(x) for x in input().split()]
l2 = [l[i] - k * i for i in range(n) if l[i] > k * i]
sl = set(l2)
base, a = 1, 0
for x in sl:
    cnt = l2.count(x)
    if cnt > a:
        base = x
        a = cnt
print(n - a)
for i in range(n):
    if l[i] < i * k + base:
        print('+', i + 1, i * k + base - l[i])
    elif l[i] > i * k + base:
        print('-', i + 1, l[i] - (i * k + base))
