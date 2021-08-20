(n, x) = map(int, input().split())
ar = list(map(int, input().split()))
st = {}
soln = 0
for el in ar:
    if el ^ x in st:
        soln += st[el ^ x]
    if el in st:
        st[el] += 1
    else:
        st[el] = 1
print(soln)
