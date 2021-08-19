n = int(input())
l = []
for i in range(1, n + 1):
    if i % 5 == 0:
        continue
    elif i % 3 == 0:
        continue
    else:
        l.append(i)
print(sum(l))
