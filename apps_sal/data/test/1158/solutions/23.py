n, m = map(int, input().split())
D = dict()
arr = list(map(int, input().split()))
for el in arr:
    if el in D.keys():
        D[el] += 1
    else:
        D[el] = 1
maxx = -1
for key in D.keys():
    if D[key] > maxx:
        maxx = D[key]
# print(maxx)
a = maxx // m
if maxx % m > 0:
    a += 1
summ = a * m
ans = 0
# print(summ)
for key in D.keys():
    ans += (summ - D[key])
print(ans)
