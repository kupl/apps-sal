n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]*n
for i in range(n):
    b[a[i]-1] += 1
c = [i for i in b if i != 0]
c.sort()
if len(c) - k > 0:
    print(sum((c[0:len(c)-k])))
else:
    print(0)
