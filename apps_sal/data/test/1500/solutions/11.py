n, k = (int(i) for i in input().split())
z = [int(i) for i in input().split()]
p = z[0]
a = z[0]
res = 0
for i in z[1:]:
    if i <= a + k:
        p = i
    elif a != p:
        res += 1
        a = p
        if i > a + k:
            res = -2
            break
        p = i
    else:
        res = -2
        break
print(res+1)
