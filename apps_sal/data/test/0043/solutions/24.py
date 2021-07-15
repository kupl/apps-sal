from functools import cmp_to_key
n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    x[i], y[i] = list(map(int, input().strip().split(" ")))

vp = []
vm = []
for i in range(n):
    if y[i] >= 0:
        vp.append(i)
    else:
        vm.append(i)


def cmp1(i, j):
    xi = (1 if x[i] > 0 else -1)
    xj = (1 if x[j] > 0 else -1)
    b = xi * x[i] * x[i] * (x[j] * x[j] + y[j] * y[j]) > xj * x[j] * x[j] * (x[i] * x[i] + y[i] * y[i])
    return (-1 if b else 1)


def cmp2(i, j):
    xi = (1 if x[i] > 0 else -1)
    xj = (1 if x[j] > 0 else -1)
    b = xi * x[i] * x[i] * (x[j] * x[j] + y[j] * y[j]) < xj * x[j] * x[j] * (x[i] * x[i] + y[i] * y[i])
    return (-1 if b else 1)


vp = sorted(vp, key=cmp_to_key(cmp1))
vm = sorted(vm, key=cmp_to_key(cmp2))
vp = vp + vm
vp.append(vp[0])

a = 0
b = 0
man = -2
mad = 1
for i in range(n):
    j = vp[i]
    k = vp[i + 1]
    tan = x[j] * x[k] + y[j] * y[k]
    p = (tan > 0)
    tan = tan * tan * (1 if p else -1)
    tad = (x[j] * x[j] + y[j] * y[j]) * (x[k] * x[k] + y[k] * y[k])
    if man * tad < tan * mad:
        man = tan
        mad = tad
        a = j
        b = k


print("{} {}".format(a + 1, b + 1))

