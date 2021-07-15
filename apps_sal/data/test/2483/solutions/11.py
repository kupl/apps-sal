def main():
    N, C = list(map(int, input().split()))
    l = []
    for _ in range(N):
        s, t, c = list(map(int, input().split()))
        l.append((s,t,c))
    l.sort(key=lambda x: x[0])
    r = []
    for i in l:
        if not r:
            r.append((i[1], i[2]))
            continue
        for j, v in enumerate(r):
            if v[0] < i[0] or (v[1] == i[2] and v[0] == i[0]):
                r[j] = (i[1], i[2])
                break
        else:
            r.append((i[1], i[2]))
        r.sort(key=lambda x:x[0])
    print((len(r)))
main()

