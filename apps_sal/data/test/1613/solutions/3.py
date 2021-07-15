n = int(input())
l = list(map(int, input().split()))
ans = 0
count = 0
d = dict()
s = set()
s1 = set()
for i in l:
    if i in s:
        d[i] += 1
    else:
        d[i] = 1
        s.add(i)
for i in range(n):
    if l[i] == 0:
        count += 1
    else:
        if l[i] not in s1:
            ans += min(d[l[i]], count)
            s1.add(l[i])
print(ans)
