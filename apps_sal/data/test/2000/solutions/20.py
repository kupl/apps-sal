n = int(input())
arr = list(map(int, input().split()))
p = []
cnt = 0
i = 2
while i < 10000000007:
    p.append(i)
    i *= 2
d = {}
for i in arr:
    if i not in d:
        d[i] = 0
    d[i] += 1
cnt = 0
for i in arr:
    d[i] -= 1
    for j in p:
        v = j - i
        if v in d:
            cnt += d[v]
print(cnt)
