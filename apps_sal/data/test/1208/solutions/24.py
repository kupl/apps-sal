n = int(input())
res = 0
nowin = []
for i in range(n):
    (op, name) = input().split()
    if op == '+':
        nowin.append(name)
        res = max(res, len(nowin))
    elif name not in nowin:
        res += 1
    else:
        nowin.remove(name)
print(res)
