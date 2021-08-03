n = int(input())
a = sorted([int(input()) for i in range(n)])
s = sum(a)
if s % 10 != 0:
    print(s)
else:
    for i in a:
        if i % 10 != 0:
            print(s - i)
            break
    else:
        print(0)
