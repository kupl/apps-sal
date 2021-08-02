def fun(n, l):
    if len(l) == 1:
        return n in l[0]
    elif len(l) == 2:
        if n < 10:
            return (n in l[0]) or (n in l[1])
        elif n < 100:
            u = n % 10
            h = int((str(n))[0])
            return (u in l[0] and h in l[1]) or (u in l[1] and h in l[0])
        else:
            return False
    else:
        if n < 10:
            return (n in l[0]) or (n in l[1]) or (n in l[2])
        elif n < 100:
            u = n % 10
            h = int((str(n))[0])
            return fun(n, [l[0], l[1]]) or fun(n, [l[0], l[2]]) or fun(n, [l[1], l[2]])


l = []
n = int(input())
for i in range(n):
    l.append([int(j) for j in input().split()])
for i in range(1, 100):
    if not(fun(i, l)):
        break
print(i - 1)
