k = int(input())
s = input().strip()
s = s.replace(' ', '-')
ts = s.split('-')
ls = [len(i) + 1 for i in ts]
ls[-1] -= 1
amin = max(ls)
als = (len(s) + k - 1) // k
ret = max(amin, als)
while True:
    nb = 0
    idx = 0
    crtsize = 0
    while nb < k:
        if crtsize + ls[idx] <= ret:
            crtsize += ls[idx]
        else:
            nb += 1
            crtsize = ls[idx]
        idx += 1
        if nb < k and idx >= len(ls):
            break
    else:
        ret += 1
        continue
    break
print(ret)
