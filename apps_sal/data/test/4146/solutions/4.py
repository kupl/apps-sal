from collections import Counter
n = int(input())
a = list(map(int, input().split()))
e = Counter(a[0::2]).most_common()
o = Counter(a[1::2]).most_common()
e.append((0, 0))
o.append((0, 0))
if e[0][0] != o[0][0]:
    print(n - o[0][1] - e[0][1])
else:
    print(min(n - o[0][1] - e[1][1], n - o[1][1] - e[0][1]))
