n = int(input())

data = []

for num in range(n):
    t = input()
    (l, r) = t.split(" ")
    l = int(l)
    r = int(r)
    data.append((l, r))

data = sorted(data, key = lambda s : s[1])

num = 1

ci = data[0]

for item in data:
    (il, ir) = item
    (cl, cr) = ci
    if (il > cr):
        ci = item
        num += 1

print(num)

