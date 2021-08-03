import operator

n, k1, k2 = list(map(int, input().split(" ")))
arrayA = list(map(int, input().split(" ")))
arrayB = list(map(int, input().split(" ")))

arraydiff = list(map(operator.sub, arrayA, arrayB))
arraydiff = list(map(abs, arraydiff))

for i in range(k1 + k2):
    index = arraydiff.index(max(arraydiff))
    if arraydiff[index] == 0:
        arraydiff[index] += 1
    else:
        arraydiff[index] -= 1
print(sum([x * x for x in arraydiff]))
