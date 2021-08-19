n = int(input())
a = list(map(int, input().split()))
t = min(a)
if t < 0:
    p = 0
    n = 0
    for i in a:
        if i > 0:
            p += i
        else:
            n += i
    print(p - n)
else:
    print(sum(a))
