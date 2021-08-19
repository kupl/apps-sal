(h, w) = map(int, input().split())
c = []
for i in range(h):
    c.append(input().split())
for i in range(h):
    s = ''.join(c[i])
    print(s + '\n' + s)
