def ri():
    return list(map(int, input().split()))


a, b, c = ri()

m = int(input())

u = []
p = []
for i in range(m):
    cost, t = input().split()
    cost = int(cost)
    if t == "USB":
        u.append(cost)
    else:
        p.append(cost)

u.sort(reverse=True)
p.sort(reverse=True)


count = 0
totcost = 0
for i in range(a):
    if len(u):
        count += 1
        totcost += u[-1]
        u.pop(-1)
    else:
        break
for i in range(b):
    if len(p):
        count += 1
        totcost += p[-1]
        p.pop(-1)
    else:
        break

for i in range(c):
    if len(u) and len(p):
        count += 1
        if u[-1] < p[-1]:
            totcost += u[-1]
            u.pop(-1)
        else:
            totcost += p[-1]
            p.pop(-1)
    elif len(u):
        count += 1
        totcost += u[-1]
        u.pop(-1)
    elif len(p):
        count += 1
        totcost += p[-1]
        p.pop(-1)
    else:
        break

print(count, totcost)
