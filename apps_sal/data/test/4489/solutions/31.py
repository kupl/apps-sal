import collections
n = int(input())
s = [''] * n
for i in range(n):
    s[i] = input()
s = collections.Counter(s)
m = int(input())
for j in range(m):
    t = input()
    if t in s:
        s[t] -= 1
print(max(0, s.most_common()[0][1]))
