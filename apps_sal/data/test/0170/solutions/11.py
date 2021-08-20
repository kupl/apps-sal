def comp(a, b):
    if len(a) != len(b):
        return False
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True


n = int(input())
a = []
b = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k1 = a[0]
k2 = b[0]
del a[0]
del b[0]
p = []
q = []
for i in a:
    p.append(i)
for i in b:
    q.append(i)
total = 0
flag = True
while True:
    x = a[0]
    y = b[0]
    if x > y:
        a.pop(0)
        b.pop(0)
        a.append(y)
        a.append(x)
    else:
        a.pop(0)
        b.pop(0)
        b.append(x)
        b.append(y)
    total += 1
    if p == a and q == b or total >= 100000:
        flag = False
        break
    if len(a) == 0 or len(b) == 0:
        break
if flag == False:
    print(-1)
elif a == []:
    print(total, 2)
else:
    print(total, 1)
