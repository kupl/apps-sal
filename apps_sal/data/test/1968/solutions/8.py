(n, v) = map(int, input().split())
qlist = []
slist = []
for i in range(n):
    slist.append(min([int(x) for x in input().split()][1:]))
for i in range(n):
    if slist[i] < v:
        qlist.append(i + 1)
print(len(qlist))
print(''.join([str(qlist[i]) + ' ' for i in range(len(qlist))]))
