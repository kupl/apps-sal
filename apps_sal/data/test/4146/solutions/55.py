from collections import Counter
n = int(input())
v = list(map(int, input().split()))

o = Counter(v[::2]).most_common()
e = Counter(v[1::2]).most_common()
if o[0][0] == e[0][0]:
    if len(o) == 1:
        print(e[0][1])
    else:
        o1, o2 = e[0][1], e[1][1]
        e1, e2 = o[0][1], o[1][1]

        ans = min(n - o1 - o2, n - e1 - e2)
        print(ans)
else:
    print(n - o[0][1] - e[0][1])
