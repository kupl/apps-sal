import collections
a = int(input())
s = [input() for i in range(a)]
c = collections.Counter(s)
b = []
for myvalue in list(c.values()):
    b.append(myvalue)
d = len(b)
ans = int(0)
for i in range(int(d)):
    if b[i] % 2 == 0:
        pass
    else:
        ans += 1
print(ans)
