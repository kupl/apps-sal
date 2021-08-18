import bisect

s = input()
t = input()
n = len(s)

dic = {}
for idx, i in enumerate(s * 2):
    if i in dic.keys():
        dic[i].append(idx)
    else:
        dic[i] = [idx]

ans, p = 0, -1
for i in t:
    if i not in dic.keys():
        print(-1)
        return
    p = dic[i][bisect.bisect_left(dic[i], p + 1)]
    if p >= n:
        p -= n
        ans += n

print(ans + p + 1)
