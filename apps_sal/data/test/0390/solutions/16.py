(n, a, b) = input().split()
n = int(n)
cost = {}
cost['0'] = int(a)
cost['1'] = int(b)
aux = min(cost['0'], cost['1'])
nuns = input().split()
resp = 0
for i in range(n):
    if nuns[i] == '2':
        if nuns[-(i + 1)] == '2':
            resp += aux
        else:
            resp += cost[nuns[-(i + 1)]]
    elif nuns[i] != nuns[-(i + 1)] and nuns[-(i + 1)] != '2':
        resp = -1
        break
print(resp)
