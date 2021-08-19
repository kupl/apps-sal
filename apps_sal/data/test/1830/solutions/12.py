n = input().split()
m = int(n[1])
n = int(n[0])
x = set()
y = set()
s = list()
e = 0
for i in range(0, m):
    t = input().split()
    x.add(int(t[0]))
    y.add(int(t[1]))
    num = (n - len(x)) * (n - len(y))
    if num < 0:
        e = i
        break
    s.append(str(num))
if e != 0:
    c = ['0' for l in range(e, m)]
    s.extend(c)
st = ' '
print(st.join(s))
