n = int(input())
d = {}
for i in range(n):
    A = int(input())
    if A not in d:
        d[A] = 1
    elif d[A] == 1:
        d[A] = 0
    else:
        d[A] = 1
print(sum(d.values()))
