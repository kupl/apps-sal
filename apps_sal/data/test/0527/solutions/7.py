import bisect
s = input()
t = input()
dic = {}
for i in range(len(t)):
    if t[i] in dic:
        continue
    if t[i] not in dic:
        dic[t[i]] = []
for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]].append(i)
for k, v in dic.items():
    if v == []:
        print(-1)
        return
n = -1
k = 0

for i in range(len(t)):
    l = bisect.bisect_right(dic[t[i]], n)
    if l < len(dic[t[i]]):
        n = dic[t[i]][l]
    else:
        n = dic[t[i]][0]
        k += 1
print(len(s) * k + n + 1)
