n = int(input())
d = {}
d['polycarp'] = 1
ans = 1
for i in range(n):
    s = input()
    a = s.split()
    a[0] = a[0].lower()
    a[2] = a[2].lower()
    d[a[0]] = d[a[2]] + 1
    ans = max(ans, d[a[0]])
print(ans)
