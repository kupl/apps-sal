n = int(input())
a = [int(input()) for _ in range(n)]
s = sum(a)
if s % 10 != 0:
    print(s)
else:
    for i in range(n):
        if min(a) % 10 != 0:
            print(s - min(a))
            break
        a.remove(min(a))
    else:
        print(0)
