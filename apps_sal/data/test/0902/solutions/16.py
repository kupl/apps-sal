n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
maxi = max(l)
a = max(l[:2])
b = min(l[:2])
l = l[2:]
g = k
while g:
    if a == maxi:
        break
    if a > b:
        g -= 1
        l.append(b)
        b = l[0]
        del l[0]
    elif b > a:
        g = k - 1
        l.append(a)
        a = b
        b = l[0]
        del l[0]
print(a)
