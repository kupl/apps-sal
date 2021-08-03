from math import log
n, k = map(int, input().split())
ai = list(map(int, input().split()))
s = set()
ai2 = []
for i in range(n):
    if ai[i] not in s:
        ai2 += [i + 1]
    s.add(ai[i])
if len(s) >= k:
    print("YES")
    for i in range(k):
        print(ai2[i], end=" ")
else:
    print("NO")
