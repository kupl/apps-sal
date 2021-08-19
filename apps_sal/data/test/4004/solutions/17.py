n = int(input())
a = [int(item) for item in input().split()]
s = set(a)
l = list(s)
if len(s) > 3:
    print(-1)
elif len(s) == 3:
    l.sort()
    if l[1] - l[0] != l[2] - l[1]:
        print(-1)
    else:
        print(l[1] - l[0])
elif len(s) == 2:
    if abs(l[0] - l[1]) % 2:
        print(abs(l[0] - l[1]))
    else:
        print(abs(l[0] - l[1]) // 2)
else:
    print(0)
