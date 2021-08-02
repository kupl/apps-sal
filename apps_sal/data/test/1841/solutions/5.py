n, m = map(int, input().split())
a = list(map(int, input().split()))
s = set([])
p = [0] * n
for i in reversed(range(n)):
    if not a[i] in s:
        s.add(a[i])
    p[i] = len(s)
for i in range(m):
    l = int(input())
    print(p[l - 1])
