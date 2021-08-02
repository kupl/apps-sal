def calc(a, b):
    if a == "S":
        if b == "E":
            return "T"
        elif b == "S":
            return "S"
        else:
            return "E"
    elif a == "E":
        if b == "E":
            return "E"
        elif b == "S":
            return "T"
        else:
            return "S"
    else:
        if b == "E":
            return "S"
        elif b == "S":
            return "E"
        else:
            return "T"


n, k = map(int, input().split())
d = {}
l = []
done = {}
for i in range(n):
    a = input()
    d[a] = 1
    l.append(a)
if n <= 2:
    print(0)
    return
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        reqd = ""
        for m in range(k):
            reqd += (calc(l[i][m], l[j][m]))
        if reqd in d:
            #print (l[i],l[j],reqd)
            if (l[i], l[j], reqd) not in done and (l[i], reqd, l[j]) not in done and (l[j], l[i], reqd) not in done and (l[j], reqd, l[i]) not in done and (reqd, l[j], l[i]) not in done and (reqd, l[i], l[j]) not in done:
                done[(l[i], l[j], reqd)] = 1
                ans += 1

print(ans)
