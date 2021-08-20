(n, m) = list(map(int, input().split()))
mas = list(map(int, input().split()))
masc = [0] * (m + 1)
for i in range(1, m + 1):
    masc[i] = mas.count(i)
i = 1
var = 0
while masc[i] > 0:
    var += masc[i] * sum(masc[i + 1:])
    i += 1
    if i >= len(masc):
        break
print(var)
