n = int(input())
lst = []
for i in range(n):
    lst.append(input())
abc = [chr(ord('a') + i) for i in range(26)]
cnt = []
for s in abc:
    temp = 100
    for i in range(n):
        temp = min(temp, lst[i].count(s))
    cnt.append(temp)
res = []
for i in range(26):
    for j in range(cnt[i]):
        res.append(abc[i])
print(''.join(res))
