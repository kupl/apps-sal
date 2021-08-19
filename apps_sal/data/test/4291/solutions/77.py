(n, q) = list(map(int, input().split()))
s = input()
con = [0]
c = False
for i in range(n):
    if s[i] == 'A':
        c = True
        con.append(con[-1])
        continue
    if c:
        if s[i] == 'C':
            con.append(con[-1] + 1)
            c = False
            continue
        else:
            con.append(con[-1])
            c = False
            continue
    con.append(con[-1])
for j in range(q):
    (l, r) = list(map(int, input().split()))
    print(max(0, con[r] - con[l]))
