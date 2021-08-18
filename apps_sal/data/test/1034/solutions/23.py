
x, y, z, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

a_max = min(k, len(a))
b_max = min(k, len(b))
c_max = min(k, len(c))

abc = []
for i in range(1, k + 1):
    if i > len(a):
        break
    for j in range(1, k // i + 1):
        if j > len(b):
            break
        for l in range(1, k // (i * j) + 1):
            if l > len(c):
                break
            abc.append(a[i - 1] + b[j - 1] + c[l - 1])

abc.sort(reverse=True)
for i in range(k):
    print((abc[i]))
