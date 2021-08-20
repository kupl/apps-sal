n = int(input())
l = list(map(int, input().split()))
v = []
l.reverse()
for i in l:
    if i not in v:
        v.append(i)
v.reverse()
print(len(v))
for i in v:
    print(i, end=' ')
