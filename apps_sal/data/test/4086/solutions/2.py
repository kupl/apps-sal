n = int(input())
x = [ int(i) for i in input().split() ][::-1]

y = set()

yy = []
for i in x:
    if i not in y:
        y.add(i)
        yy.append(i)


yy = yy[::-1]
print(len(yy))
for i in yy:
    print(i,end=" ")

