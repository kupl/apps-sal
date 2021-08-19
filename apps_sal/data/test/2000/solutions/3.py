n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
found = {}
x = 1
out = 0
for j in a:
    while 2 ** x <= j:
        x += 1
    left = 2 ** x - j
    try:
        out += found[left]
    except:
        pass
    try:
        found[j] += 1
    except:
        found[j] = 1
print(out)
