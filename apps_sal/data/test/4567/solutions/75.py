n = int(input())
s = []
for i in range(n):
    s += [int(input())]
s = sorted(s)
a = sum(s)
if a % 10 != 0:
    print(a)
    return
else:
    for i in range(n):
        if s[i] % 10 != 0:
            a -= s[i]
        if a % 10 != 0:
            print(a)
            f = 0
            return
        else:
            f = 1
if f:
    print(0)
