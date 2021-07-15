n, b = list(map(int, input().split()))
a = list(map(int, input().split()))
e = [0] * len(a)
o = [0] * len(a)

for i, elem in enumerate(a):
    e[i] = e[i - 1]
    o[i] = o[i - 1]

    if elem % 2 == 0:
        e[i] += 1
    else:
        o[i] += 1

cuts = 0
price = 0

while True:
    min_i = -1
    min_val = 1e9
    for i in range(len(a) - 1):
        if e[i] == o[i]:
            if abs(a[i] - a[i + 1]) < min_val:
                min_val = abs(a[i] - a[i + 1])
                min_i = i
    if min_i != -1 and price + min_val <= b:
        cuts += 1
        price += min_val
        a[min_i] = 1e9
    else:
        break

print(cuts)

