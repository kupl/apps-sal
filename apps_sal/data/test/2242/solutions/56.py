from collections import Counter
s = input()

ls = len(s)
t = [0]
j = 1
for i in range(ls):
    u = (int(s[ls-1-i])*j + t[-1]) % 2019
    t.append(u)
    j = (j * 10) % 2019
c = Counter(t)
k = list(c.keys())
ans = 0
for i in k:
    ans += c[i]*(c[i]-1)/2
print(int(ans))
