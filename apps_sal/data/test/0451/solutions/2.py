n, k = map(int, input().split())
a = list(map(int, input().split()))
b = input()
r = []
o = []
w = []
for i in range(n):
    if (b[i] == 'R'):
        r.append(a[i])
    elif (b[i] == 'O'):
        o.append(a[i])
    else:
        w.append(a[i]);
r.sort()
o.sort()
w.sort()
r.reverse()
o.reverse()
w.reverse()
if k == 1 or (len(r) * len(o) == 0 and len(o) * len(w) == 0):
    print('-1')
else:
    r1 = 0
    o1 = 0
    ans1 = 0
    o2 = 0
    w2 = 0
    ans2 = 0
    if (len(r) + len(o) >= k and len(r) * len(o) != 0):
        r1 = 1
        o1 = 1
        ans1 = r[0] + o[0]
        while(r1 + o1 < k):
            if (o1 >= len(o) or (r1 < len(r) and r[r1] > o[o1])):
                ans1 += r[r1]
                r1 += 1
            else:
                ans1 += o[o1]
                o1 += 1
    if (len(o) + len(w) >= k and len(o) * len(w) != 0):
        o2 = 1
        w2 = 1
        ans2 = o[0] + w[0]
        while(o2 + w2 < k):
            if (o2 >= len(o) or (w2 < len(w) and w[w2] > o[o2])):
                ans2 += w[w2]
                w2 += 1
            else:
                ans2 += o[o2]
                o2 += 1
    if (max(ans1, ans2) == 0):
        print("-1")
    else:
        print(max(ans1, ans2))
