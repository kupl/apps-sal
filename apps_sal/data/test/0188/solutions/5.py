n, m = list(map(int, input().split()))
z = list(map(int, input().split()))
h = z[:]
double = 2 * n
four = n
jj = []
for i in range(len(h)):
    while four > 0 and h[i] >= 4:
        h[i] -= 4
        four -= 1
    if (h[i] != 0):
        jj.append(h[i])
ss = []
for i in range(len(jj)):
    while four > 0 and jj[i] >= 3:
        jj[i] -= 3
        four -= 1
    if jj[i] != 0:
        ss.append(jj[i])

tt = []
for i in range(len(ss)):
    while double > 0 and ss[i] >= 2:
        ss[i] -= 2
        double -= 1
    if ss[i]:
        tt.append(ss[i])

places = double + four * 2
gg = []
for i in range(len(tt)):
    while four > 0 and tt[i] >= 2:
        tt[i] -= 2
        places -= 1
        four -= 1
    if tt[i]:
        gg.append(tt[i])
if (sum(gg) <= places):
    print("YES")
else:
    print("NO")
