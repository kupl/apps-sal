n = int(input())
result = 0
weight = [0 for i in range(10)]
canzero = [True for i in range(10)]
for _ in range(n):
    x = list(str(input()))
    canzero[ord(x[0]) - 97] = False
    x.reverse()
    for i in range(len(x)):
        weight[ord(x[i]) - 97] += pow(10, i)
# print(canzero)
# print(weight)
zero = 10
cl = weight[:]
while True:
    candidate = max(cl)
    i = cl.index(candidate)
    if canzero[i]:
        zero = i
        break
    else:
        cl[i] = -1
weight.remove(weight[zero])
weight = sorted(weight)
weight.reverse()
for i in range(1, 10):
    result += i * weight[i - 1]
# print(cl, zero, weight)
print(result)

