n,m =map(int,input().split())
l = list()
out = [0] * n
for i in range(m):
    s1,d1,c1 = map(int,input().split())
    l.append((s1,d1,c1,i))
l.sort(key=lambda x:x[1])
can = True
for j in l:
    out[j[1] - 1] = m + 1
for i in l:
    c = i[2]
    for t in range(i[0],i[1]):
        if out[t - 1] == 0 and c > 0:
            out[t - 1] = i[3] + 1
            c -= 1
        if c == 0:
            break
    if c != 0:
        print(-1)
        can = False
        break

if can is True:
    print(" ".join(map(str,out)))
