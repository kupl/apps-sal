def check(x, y, z, i, ops):
    if x == 1 and y == 1 and z == 0 and i < len(ops) - 1:
        return (ops[i], ops[i + 1]) in [("AB", "AC"), ("BC", "AB"), ("AC", "AB")]
    return (x <= y)


A = 0
B = 1
C = 2
nabc = [int(_x) for _x in input().split()]
n = nabc[0]
abc = nabc[1:]
ops = []
for i in range(n):
    ops.append(input())

result = []
for i in range(n):
    op = ops[i]
    if op == "AB":
        (s, t, u) = (A, B, C)
    elif op == "BC":
        (s, t, u) = (B, C, A)
    else:
        (s, t, u) = (A, C, B)
    if check(abc[s], abc[t], abc[u], i, ops):
        result.append(s)
        abc[s] += 1
        abc[t] -= 1
    else:
        result.append(t)
        abc[s] -= 1
        abc[t] += 1
    if abc[s] < 0 or abc[t] < 0:
        print("No")
        break
else:
    print("Yes")
    for r in result:
        if r == A:
            print("A")
        if r == B:
            print("B")
        if r == C:
            print("C")
