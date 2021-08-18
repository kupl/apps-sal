t = int(input())
for r in range(t):
    q = input()
    o = [w for w in range(len(q)) if q[w] in 'nw']
    e = []
    for w in o:
        if q[w - 1:w + 2] in ['two', 'one']:
            e += [[w, 1]]
    e.sort()
    for w in range(len(e) - 1):
        if e[w][0] + 2 == e[w + 1][0]:
            e[w][0] += 1
            e[w + 1][1] = 0
    e = [w[0] + 1 for w in e if w[1]]
    print(len(e))
    print(*e)
