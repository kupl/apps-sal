n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())
one = l.index(max(l))
two = r.index(min(r))
if one == 0:
    f = min(r[1:]) - max(l[1:])
elif one == n - 1:
    f = min(r[:n - 1]) - max(l[:n - 1])
else:
    f = min(min(r[:one]), min(r[one + 1:])) - max(max(l[:one]), max(l[one + 1:]))
if two == 0:
    s = min(r[1:]) - max(l[1:])
elif two == n - 1:
    s = min(r[:n - 1]) - max(l[:n - 1])
else:
    s = min(min(r[:two]), min(r[two + 1:])) - max(max(l[:two]), max(l[two + 1:]))
print(max(max(f, s), 0))
