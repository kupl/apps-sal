(h, w) = map(int, input().split())
c = []
for _ in range(h):
    c.append(list(input()))
for i in range(2 * h):
    print(''.join(c[i // 2]))
