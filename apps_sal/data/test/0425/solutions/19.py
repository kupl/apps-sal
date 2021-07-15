a, b = map(lambda x: int(x), input().split())
k = 0
s = 1
f = True
while k < s:
    a = a - b
    if a <= 0:
        break
    c = a
    k += 1
    s = 1
    while c != 1:
        s += c % 2
        c = c // 2

q = k - s
q1 = k
for i in range(q):
    a = a - b
    if a <= 0:
        break
    c = a
    k += 1
    s = 1
    while c != 1:
        s += c % 2
        c = c // 2

    if s == k:
        print(s)
        f = False
        break
if f and a > 0:
    print(q1)

if a <= 0:
    print(-1)
