__author__ = 'user'
n = int(input())
s = set()
ans = 0
x = set()
a = ["0"] * n
b = [0] * n
for i in range(n):
    type, id = map(str, input().split())
    a[i], b[i] = type, id
    id = int(id)
    if type == "+":
        s.add(id)
    elif type == "-":
        if id in s:
            s.remove(id)
        elif id not in s:
            x.add(id)

s.clear()
s = set(x)
ans = max(ans, len(s))
for i in range(n):
    type, id = a[i], b[i]
    id = int(id)
    if type == "+":
        s.add(id)
    elif type == "-":
        if id in s:
            s.remove(id)
    #print(s)
    ans = max(ans, len(s))
print(ans)
