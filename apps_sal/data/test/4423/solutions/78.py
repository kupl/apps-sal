n = int(input())
tbl = []
s = []
p = []
for i in range(n):
    l = list(map(str, input().split()))
    l[1] = int(l[1])
    l2 = [l[1], l[0], i + 1]
    tbl.append(l2)
    s.append(l2[1])
    p.append(l2[0])
p.sort()
p.reverse()
tbl2 = []
for i in range(n):
    for j in range(n):
        if tbl[j][0] == p[i]:
            tbl2.append(tbl[j])
s = list(set(s))
s.sort()
for i in range(len(s)):
    for j in range(len(tbl2)):
        if tbl2[j][1] == s[i]:
            print(tbl2[j][2])
