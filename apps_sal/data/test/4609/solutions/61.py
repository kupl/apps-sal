import collections
n = int(input())
a = []
for i in range(n):
    A = int(input())
    a.append(A)
c = collections.Counter(a)
ans = 0
for i in c:
    if c[i] % 2 == 1:
        ans += 1
print(ans)
