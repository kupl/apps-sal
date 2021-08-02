n, m = list(map(int, input().split()))
a = []
for i in range(n):
    s = input()
    v = []
    for i in s:
        if i == '.':
            v.append(0)
        else:
            v.append(1)
    a.append(v)
sp = 0
pod = 0
for i in range(m - 1):
    s1 = 0
    s2 = 0
    for j in range(n):
        s1 += a[j][i]
        s2 += a[j][i + 1]
        if s1 - s2 < 0 and abs(s1 - s2) > pod:
            pod = abs(s1 - s2)
        elif s1 - s2 > 0 and abs(s1 - s2) > sp:
            sp = abs(s1 - s2)
print(pod, sp)
