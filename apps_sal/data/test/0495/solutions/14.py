from sys import stdin
a, k = stdin.readline().split()
a, k = list(a), int(k)
b = sorted(a, reverse = True)
for i in range(len(a)):
    for x in b:
        if a[i] == x: break
        j = a.index(x, i)
        if j - i > k: continue
        k -= j - i
        a[i: j + 1] = [a[j]] + a[i: j]
        break
    b.remove(a[i])
print(''.join(a))
