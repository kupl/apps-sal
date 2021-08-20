(h, w) = map(int, input().split())
a = []
for _ in range(h):
    a.append('#' + input() + '#')
sharp = '#' * (w + 2)
print(sharp)
for j in range(0, h):
    print(a[j])
print(sharp)
