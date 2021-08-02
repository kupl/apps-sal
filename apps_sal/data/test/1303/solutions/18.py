p, q, l, r = list(map(int, input().split(' ')))
P = []
Q = []
for i in range(p):
    P.append(list(map(int, input().split(' '))))
for i in range(q):
    Q.append(list(map(int, input().split(' '))))
res = 0
for i in range(l, r + 1):
    index_q = 0
    index_p = 0
    for j in range(p + q):
        if index_q == q or index_p == p:
            break
        if P[index_p][1] < Q[index_q][0] + i:
            index_p += 1
        elif Q[index_q][1] + i < P[index_p][0]:
            index_q += 1
        else:
            res += 1
            break
print(res)
