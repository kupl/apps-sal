n = int(input())
s = []
cnt = [0] * 5
l = ['M', 'A', 'R', 'C', 'H']
ans = 0
for i in range(n):
    s.append(input())
for i in s:
    if i[0] in l:
        cnt[l.index(i[0])] += 1
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += cnt[i] * cnt[j] * cnt[k]
print(ans)
