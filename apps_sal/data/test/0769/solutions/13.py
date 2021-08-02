V = set()
a, b, c = (int(i) for i in input().split())
i = 1
d = -1
shit = True
while a % b not in V:
    a = a % b
    V.add(a)
    a = a * 10
    d = a // b
    if d == c:
        print(i)
        shit = False
        break
    i += 1
if shit:
    print(-1)
