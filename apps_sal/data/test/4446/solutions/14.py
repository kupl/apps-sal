(n, a, b, k) = map(int, input().split())
h = input().split()
for i in range(n):
    h[i] = int(h[i])
ls = []
for i in range(n):
    if h[i] % (a + b) == 0:
        h[i] = a + b
        if h[i] % a == 0:
            mauka = h[i] // a
        else:
            mauka = h[i] // a + 1
        ls.append(mauka - 1)
    else:
        h[i] = h[i] % (a + b)
        if h[i] <= a:
            ls.append(0)
        else:
            if h[i] % a == 0:
                mauka = h[i] // a
            else:
                mauka = h[i] // a + 1
            ls.append(mauka - 1)
ls.sort()
count = 0
for i in range(n):
    if ls[i] <= k:
        k -= ls[i]
        count += 1
print(count)
