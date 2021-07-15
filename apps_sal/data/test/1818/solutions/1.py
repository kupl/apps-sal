n = int(input())
t = list(map(int, input().split()))
p, s = {}, 0

for i in t:
    j = sum(k == '1' for k in format(i, 'b'))
    p[j] = p.get(j, 0) + 1
for j in p:
    s += p[j] * (p[j] - 1)
print(s // 2)
