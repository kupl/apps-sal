n = int(input())
s1 = list(map(int, input().split()))
s1.pop(0)
s2 = list(map(int, input().split()))
s2.pop(0)
c = 0
while s1 and s2 and (c < 10 ** 5):
    if s1[0] > s2[0]:
        s1.append(s2[0])
        s1.append(s1[0])
    else:
        s2.append(s1[0])
        s2.append(s2[0])
    s1.pop(0)
    s2.pop(0)
    c += 1
if not s1:
    print(c, 2)
elif not s2:
    print(c, 1)
else:
    print(-1)
