from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
l1 = []
l2 = []
da = defaultdict(int)
db = defaultdict(int)
work = True
for i in a:
    if da[i] == 0:
        l1.append(i)
        da[i] = 1
    elif db[i] == 0:
        l2.append(i)
        db[i] = 1
    else:
        work = False

if work:
    print("YES")
    print(len(l1))
    print(*sorted(l1))
    print(len(l2))
    l2 = sorted(l2)
    l2 = l2[::-1]
    print(*l2)
else:
    print("NO")
