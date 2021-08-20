(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [b[i] // a[i] for i in range(n)]
c1 = [b[i] % a[i] for i in range(n)]
while k > 0:
    x = min(c)
    ind = c.index(x)
    b[ind] += 1
    k -= 1
    c[ind] = b[ind] // a[ind]
    c1[ind] = b[ind] % a[ind]
print(min(c))
