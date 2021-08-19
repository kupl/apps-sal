N = int(input())
ss = dict()
for i in range(N):
    s = input()
    ss[s] = ss.get(s, 0) + 1
sss = [(-b, a) for (a, b) in list(ss.items())]
sss.sort()
maxa = sss[0][0]
for (a, b) in sss:
    if maxa != a:
        break
    print(b)
