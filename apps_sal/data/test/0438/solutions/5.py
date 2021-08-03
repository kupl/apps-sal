q = int(input())
a = [1]
q -= 1
l = 1
while q > a[l - 1]:
    q -= l + 1
    a.append(l + 1)
    l += 1
a[l - 1] += q
print(len(a))
for i in a:
    print(i, end=' ')
