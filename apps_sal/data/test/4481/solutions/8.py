import collections
n = int(input())
A = []
for i in range(n):
    a = str(input())
    A.append(a)
c = collections.Counter(A)
ma = c.most_common()[0][1]
C = [i[0] for i in c.items() if i[1] >= ma]
C.sort(reverse=False)
for j in range(len(C)):
    print(C[j])
