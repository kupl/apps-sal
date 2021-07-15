n = int(input())
a = [int(i) for i in input().split()]
f1 = f2 = False
for i in a:
    if i % 2 == 0:
        f1 = True
    else:
        f2 = True
if f1 and f2:
    print(*sorted(a))
else:
    print(*a)
