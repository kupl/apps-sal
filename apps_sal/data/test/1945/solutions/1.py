q = int(input())
current = []
begin = []
for i in range(q):
    (old, new) = input().split()
    for ind in range(len(current)):
        if current[ind] == old:
            current[ind] = new
            break
    else:
        begin.append(old)
        current.append(new)
print(len(begin))
for el in zip(begin, current):
    print(el[0], el[1])
