a = []
for x in range(int(input())):
    a.append(1)
    while len(a) > 1 and a[-1] == a[-2]:
        a.pop()
        a.append(a.pop() + 1)
print(*a)
