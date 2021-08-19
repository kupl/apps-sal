(h, w) = map(int, input().split())
a = [input() for _ in range(h)]
s = ''
for i in range(w + 2):
    s += '#'
print(s)
for i in a:
    t = list(i)
    t.insert(0, '#')
    t.append('#')
    print(''.join(t))
print(s)
