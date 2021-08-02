*I, = list(map(int, input().split()))
for p in range(1 << 4):
    s, r = 0, 0
    for i in range(4):
        if p & (1 << i): s += I[i]
        else: r += I[i]
    if s == r:
        print('Yes')
        return
print('No')
