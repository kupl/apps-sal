n = int(input())
s = input()
s = s.split()
a = []
for i in range(n):
    a.append(int(s[i]))
su = 0
d = {}
a.sort(reverse=True)
for i in range(len(a)):
    if a[i] not in d:
        su += a[i]
        d[a[i]] = 1
    else:
        t = a[i] - 1
        while t >= 1 and t in d:
            t -= 1
        su += t
        d[t] = 1
print(su)
