N = int(input())
Alist = list(map(int, input().split()))
Aplu = []
Amin = dict()
for i in range(N):
    A = Alist[i]
    Aplu.append(A + (i + 1))
    if i + 1 - A not in Amin:
        Amin[i + 1 - A] = 1
    else:
        Amin[i + 1 - A] += 1
Answer = 0
for k in Aplu:
    if k in Amin:
        Answer += Amin[k]
print(Answer)
