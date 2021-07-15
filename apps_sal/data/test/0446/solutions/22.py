n = int(input())
a = []
tmp = 0
k = 1
while tmp * 2 < n:
    tmp = (2**k - 1) * (2**(k - 1))
    a.append(tmp)
    k += 1
for i in range(len(a) - 1, -1, -1):
    if n % a[i] == 0:
        print(a[i])
        return

