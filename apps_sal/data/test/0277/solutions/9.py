n, a, b = list(map(int, input().split()))
a -= 1
b -= 1
q = []
for i in range(n // 2):
    q.append(((2 * i, 2 * i + 1), 1))

def wi(p):
    if a in p and b in p:
        return True
    return False

def ch(p):
    if a in p:
        return a
    if b in p:
        return b
    return p[0]

while 1:
    if len(q) == 1:
        print('Final!')
        return
    p1 = q[0][0]
    p2 = q[1][0]
    if wi(p1):
        print(q[0][1])
        return
    if wi(p2):
        print(q[1][1])
        return
    q.append(((ch(p1), ch(p2)), q[0][1] + 1))
    del q[0]
    del q[0]

