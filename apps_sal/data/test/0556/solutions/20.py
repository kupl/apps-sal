l, r, k = list(map(int, input().split()))
x = 1
while x < l:
    x *= k
a = []
while x <= r:
    a.append(x)
    x *= k

print(-1 if not a else ' '.join(list(map(str, a))))
