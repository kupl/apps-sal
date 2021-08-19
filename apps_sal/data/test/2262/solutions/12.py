n = int(input())
rec = []
p = list(input().split())
for i in range(n):
    a = list(p[i])
    a = sorted(a)
    s = sorted(list(set(a)))
    if s not in rec:
        rec.append(s)
print(len(rec))
