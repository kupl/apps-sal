from collections import Counter
n = int(input())
s = [None] * n
for i in range(n):
    s[i] = input().rstrip()
m = int(input())
t = [None] * m
for i in range(m):
    t[i] = input().rstrip()
ctr = Counter(s) - Counter(t)
if ctr:
    print(ctr.most_common(1)[0][1])
else:
    print(0)
