import collections
N = int(input())
L = []
for i in range(N):
    L.append(input())
C = collections.Counter(L)
Max = C.most_common()[0][1]
l = [i[0] for i in C.items() if i[1] == Max]
print(*sorted(l), sep='\n')
