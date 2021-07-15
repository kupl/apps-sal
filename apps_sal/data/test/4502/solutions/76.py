n = int(input())
a_list = [int(x) for x in input().split()]
b = []
c = []
for i, a in enumerate(a_list):
    if i % 2 == 0:
        b.append(a)
    else:
        c.append(a)
if n % 2 == 0:
    d = list(reversed(c)) + b
else:
    d = list(reversed(b)) + c
print(*d)
