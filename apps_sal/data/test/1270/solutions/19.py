a = int(input())
l = []
while a > 3:
    l.append(2)
    a -= 2
if a == 3:
    l.append(3)
elif a == 2:
    l.append(2)

print(len(l))
print(*l)
