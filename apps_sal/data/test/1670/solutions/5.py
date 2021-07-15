tn = [input(), input()]
t2i = {'h': 0, 'a': 1}
c2s = {'y': 1, 'r': 2}
st = [[0] * 100, [0] * 100]
for i in range(int(input())):
    m, t, p, c = input().split()
    m = int(m)
    t = t2i[t]
    p = int(p)
    s = c2s[c]
    if st[t][p] < 2:
        st[t][p] += s
        if st[t][p] >= 2:
            print(tn[t], p, m)
