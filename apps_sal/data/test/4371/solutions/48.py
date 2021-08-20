s = list(input())
t = [int(a) for a in s]
n = int(len(t))
ans = 0
b = 0
list1 = []
s = 1000
for i in range(n - 2):
    u = [t[i], t[i + 1], t[i + 2]]
    v = ''.join(map(str, u))
    w = int(v) - 753
    list1.append(w)
u = int(len(list1))
for i in range(u):
    if abs(list1[i]) - abs(s) <= 0:
        s = list1[i]
    else:
        pass
print(abs(s))
