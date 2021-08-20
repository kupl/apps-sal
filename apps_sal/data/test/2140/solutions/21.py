s = input()
m2 = int(input())
a = list(map(int, input().split()))
m = {}
m1 = set()
for i in range(m2):
    if a[i] not in m1:
        m1.add(a[i])
        m[a[i]] = 1
    else:
        m[a[i]] += 1
if 1 in m1:
    k = [m[1]]
else:
    k = [0]
for i in range(1, len(s) // 2):
    if i + 1 in m1:
        k.append(k[-1] + m[i + 1])
    else:
        k.append(k[-1])
s1 = []
for i in range(len(s)):
    s1.append(s[i])
for i in range(len(s) // 2):
    if k[i] % 2 == 1:
        t = s1[len(s) - i - 1]
        s1[len(s) - i - 1] = s[i]
        s1[i] = t
for i in range(len(s1)):
    print(s1[i], end='')
