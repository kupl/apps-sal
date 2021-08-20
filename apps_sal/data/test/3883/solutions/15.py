ent = input().split()
x = int(ent[0])
y = int(ent[1])
qn = ((x + y) / (2 * y)).__trunc__()
if qn == 0:
    print(-1)
else:
    n = (x + y) / (2 * qn)
    print(n)
