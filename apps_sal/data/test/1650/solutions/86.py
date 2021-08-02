def mempow(a, b, m):
    temp = 1
    yield temp
    for i in range(b):
        temp = temp * a % m
        yield temp


L = open(0).read().split()[0]
m = 1000000007
mem2 = []
mem3 = []
m2append = mem2.append
m3append = mem3.append
for x in mempow(2, L.count('1'), m):
    m2append(x)
for x in mempow(3, len(L) - 1, m):
    m3append(x)
ans = mem3[len(L) - 1]
appeared = 1
for i in range(1, len(L)):
    if L[i] == '1':
        ans = (ans + mem2[appeared] * mem3[len(L) - i - 1]) % m
        appeared += 1
ans = (ans + mem2[appeared]) % m
print(ans)
