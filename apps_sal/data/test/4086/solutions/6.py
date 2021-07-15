n = int(input())
l = list(map(int, input().split(' ')))
s = set()
l1 = list()
l.reverse()
for i in l:
    if not i in s:
        l1.append(i)
        s.add(i)
l1.reverse()
print(len(l1))
for i in l1:
    print(i, end=' ')
