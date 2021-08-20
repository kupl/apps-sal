(p, q, l, r) = tuple(map(int, input().split(' ')))
IP = [False] * 1001
IQ = [False] * 1001
for i in range(p):
    (a, b) = tuple(map(int, input().split(' ')))
    IP[a:b + 1] = [True] * (b - a + 1)
for i in range(q):
    (a, b) = tuple(map(int, input().split(' ')))
    IQ[a:b + 1] = [True] * (b - a + 1)
li = []
li = (1 for i in range(l, r + 1) if any((True for j in range(1001 - i) if IP[i + j] and IQ[j])))
print(sum(li))
