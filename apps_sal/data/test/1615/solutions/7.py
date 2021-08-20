a = input().split()
n = int(a[0])
k = int(a[1])
p = 0
for i in range(n):
    b = input().split()
    p = int(b[1]) - int(b[0]) + 1 + p
if p % k == 0:
    print(0)
else:
    s = (k - p % k) % k
    print(s)
