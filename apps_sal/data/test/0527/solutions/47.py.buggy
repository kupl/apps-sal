import bisect

s = input()
t = input()
n = len(s) * 2

dic = {}
for idx, i in enumerate(s * 2):
    if i in dic.keys():
        dic[i].append(idx)
    else:
        dic[i] = [idx]

# print(dic)

ans = k = 0
before = '-1'
for i in t:
    if i not in dic.keys():
        print(-1)
        return
    t = bisect.bisect_left(dic[i], ans % n)
    if before == i:
        t += 1
    if len(dic[i]) == t:
        t = 0
        k += n
    ans = dic[i][t] + k
    before = i

print(ans + 1)
