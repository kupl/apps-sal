a, k = list(map(int, input().split()))

a = list(str(a))
b = ''

while a:
    e = max(a[:k + 1])
    ind = a.index(e)
    b += e
    k -= ind
    a.pop(ind)

print(b)
