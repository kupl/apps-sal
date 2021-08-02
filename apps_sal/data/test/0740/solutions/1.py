k, n1, n2, n3, t1, t2, t3 = map(int, input().split())
x1 = x2 = x3 = 0
T1, T2, T3 = [0] * n1, [0] * n2, [0] * n3
for i in range(k):
    T1[x1] += t1
    T2[x2] = max(T1[x1], T2[x2]) + t2
    T3[x3] = max(T2[x2], T3[x3]) + t3
    x1 += 1
    x2 += 1
    x3 += 1
    if x1 == n1:
        x1 = 0
    if x2 == n2:
        x2 = 0
    if x3 == n3:
        x3 = 0
print(T3[x3 - 1])
