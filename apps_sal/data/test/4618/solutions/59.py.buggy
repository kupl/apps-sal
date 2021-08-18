s = input()
k = int(input())
l = "abcdefghijklmnopqrstuvwxyz"
d = {}

for i in range(26):
    cnt = s.count(l[i])
    pre = 0
    if cnt > 0:
        for j in range(cnt):
            pos = s.find(l[i], pre)
            pre = pos + 1
            for m in range(min(len(s) - pos, k)):
                if s[pos:pos + m + 1] not in d:
                    d[s[pos:pos + m + 1]] = 1
    if len(d) >= k:
        dl = []
        for i in d.keys():
            dl.append(i)
        dl.sort()
        print(dl[k - 1])
        return
