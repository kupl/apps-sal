

n = int(input())
x = [int(i) for i in input().split()]
otv = []
i = 0
while i < n:
    if len(otv) < 2:
        otv.append(x[i])
        i += 1
        continue
    if otv[len(otv) - 1] == otv[len(otv) - 2]:
        otv.pop()
        otv[len(otv) - 1] += 1
    else:
        otv.append(x[i])
        i += 1
while len(otv) >= 2 and otv[len(otv) - 1] == otv[len(otv) - 2]:
    otv.pop()
    otv[len(otv) - 1] += 1
print(len(otv))
for i in otv:
    print(i, end=" ")
