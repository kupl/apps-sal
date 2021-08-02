n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = {}
var = []

for x, y in zip(a, b):
    old = tmp.get(x, -1)
    if y > old:
        if old > -1:
            var.append(old)
        tmp[x] = y
    else:
        var.append(y)

var.sort()
print(sum(var[:k - len(tmp)]))
