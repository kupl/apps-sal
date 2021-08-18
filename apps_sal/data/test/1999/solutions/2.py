n = int(input())


def insert(x, d, i, s):
    s.add(x)
    try:
        d[x].append(i)
        if(len(d[x]) == 2):
            d[x] = []
            s.remove(x)
            insert(2 * x, d, i, s)
    except:
        d[x] = [i]


a = list(map(int, input().split()))

d = dict()
s = set()

for i in range(n):
    insert(a[i], d, i, s)
fin = []
for i in d.keys():
    for j in d[i]:
        fin.append([j, i])
fin.sort()
print(len(fin))
for i in fin:
    print(i[1], end=' ')
