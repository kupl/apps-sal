from collections import Counter
n = int(input())
L = list(map(int, input().split()))
L.sort()

L = Counter(L)

cnt = 0
one = 0
for v in L.values():
    if v % 2 == 0:
        cnt += 1
    else:
        one += 1
if cnt % 2 == 0:
    one += cnt
else:
    one += (cnt - 1)
print(one)
