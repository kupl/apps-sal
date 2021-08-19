n = int(input())
d = {}
for i in range(n):
    (old, new) = input().split()
    already = True
    for i in d:
        if old == d[i]:
            d[i] = new
            already = False
    if already:
        d[old] = new
print(len(d))
for i in d.keys():
    print(str(i) + ' ' + str(d[i]))
