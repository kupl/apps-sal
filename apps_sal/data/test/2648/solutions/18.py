import collections
n = int(input())
a = list(map(int, input().split()))
d = set(a)
c = collections.Counter(a)
b = 0
for i in c:
    if c[i] >= 2:
        b += c[i] - 1
if b % 2 == 1:
    ans = len(d) - 1
else:
    ans = len(d)
print(ans)
