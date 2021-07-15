n = int(input())
a = [int(x) for x in input().split()]
b = sorted(set(a))

if len(b) == 1:
    print(0)
elif len(b) == 2:
    b.sort()
    if sum(b) % 2 == 0:
        print((b[1] - b[0])//2)
    else:
        print(b[1] - b[0])
elif len(b) == 3:
    b.sort()
    if b[0] + b[2] == 2*b[1]:
        print(b[1] - b[0])
    else:
        print(-1)
else:
    print(-1)
