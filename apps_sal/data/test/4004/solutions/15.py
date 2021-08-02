from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a.sort()
mn = a[0]
mx = a[-1]
c = Counter(a)
med = -1
for i in c:
    if mn < i < mx:
        med = i
if len(c) > 3:
    print(-1)
elif len(c) == 3:
    if med - mn == mx - med:
        print(med - mn)
    else:
        print(-1)
elif len(c) == 2:
    print((mx - mn) // 2 if (mx - mn) % 2 == 0 else mx - mn)
else:
    print(0)
