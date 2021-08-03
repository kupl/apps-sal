n, h = list(map(int, input().split()))
a = [0] * n
b = [0] * n
for i in range(n):
    ai, bi = list(map(int, input().split()))
    a[i] = ai
    b[i] = bi

a.sort(reverse=True)
b.sort(reverse=True)
b_select = []
for i in range(n):
    if b[i] < a[0]:
        break
    else:
        b_select.append(b[i])

if sum(b_select) >= h:
    for i in range(n):
        h -= b_select[i]
        if h <= 0:
            break
    counter = i + 1
else:
    h -= sum(b_select)
    counter = len(b_select)
    counter += (h + a[0] - 1) // a[0]

print(counter)
