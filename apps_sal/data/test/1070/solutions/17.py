n, k = [int(x) for x in input().split()]
a = [x for x in input().split()]

counter = 0
r = []
pred = a[0]
for i in range(1, n):
    if a[i] != pred:
        counter += 1
    else:
        r.append(counter + 1)
        counter = 0
    pred = a[i]
if counter != 0:
    r.append(counter + 1)

if r != []:
    print(max(r))
else:
    print(1)
