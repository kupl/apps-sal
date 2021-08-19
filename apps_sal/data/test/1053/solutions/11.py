nn = input()
n = int(nn)
st = 0
dv = 1
step = []
while dv <= n:
    step.append(dv)
    dv = dv * 2
    st += 1
step.append(dv)
step.append(dv * 2)
otv = 0
f = 1
q = 0
while f != 0:
    if n == 0:
        break
    if n == 1:
        break
    for i in range(len(step)):
        if step[i] > n:
            q = i - 1
            break
    if n == step[q]:
        otv += step[q - 1] * q
        n -= step[q]
    else:
        otv += step[q] + step[q - 1] * q
        n -= step[q]
print(otv)
