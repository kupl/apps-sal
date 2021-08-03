q = int(input())
info = [[int(i) for i in input().split()] for k in range(q)]

for inf in info:
    c, m, x = inf
    print(min([c, m, int((c + m + x) / 3)]))
