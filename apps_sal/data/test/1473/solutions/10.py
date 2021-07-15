
n = int(input())

s = dict()
for i in range(n):
    (a,b) = [int(element) for element in input().split(' ')]
    s[a] = b

v = []
v.append(0)
t = set(s.values())
for key in list(s.keys()):
    if(key not in t):
        v.append(key)
        break
for i in range(n-1):
    v.append(s[v[-2]])
v = [str(elem) for elem in v]
print(' '.join(v[1:]))

