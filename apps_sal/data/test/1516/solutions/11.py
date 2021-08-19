# your code goes here
a = int(input())
li = list(map(int, input().split()))
b = []
zz = len(str(li[0]))
op = [10**i for i in range(20)]
r = 998244353
for i in li:
    i = str(i)
    p = 0
    q = 0
    z = 2 * zz - 1
    z1 = 2 * zz - 2
    for j in i:
        j = int(j)
        p += j * op[z]
        q += j * op[z1]
        z -= 2
        z1 -= 2
    b.append((((p + q) % r) * (a)) % r)
ans = 0
for i in b:
    ans += i % r
print(ans % r)
