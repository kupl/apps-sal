n = int(input())
a = {i: 0 for i in range(10**5 + 1)}
s = 0
for i in map(int, input().split()):
    s += i
    a[i] += 1
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    s -= b * a[b] - c * a[b]
    a[c] += a[b]
    a[b] = 0
    print(s)
