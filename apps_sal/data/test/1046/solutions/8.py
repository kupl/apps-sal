input()
(a, i, c) = (input().split(), 0, 0)
a.sort()
while i < len(a):
    j = a.count(a[i])
    if a[i] != '0':
        if j == 2:
            c += 1
        elif j > 2:
            c = -1
            break
    i += j
print(c)
