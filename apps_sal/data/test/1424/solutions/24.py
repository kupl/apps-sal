def diff(a, b):
    while len(a) < len(b):
        a = '0' + a
    while len(b) < len(a):
        b = '0' + b
    ret = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ret += 1
    return ret


(n, m, k) = list(map(int, input().split()))
L = []
for i in range(m):
    x = int(input())
    L.append(bin(x)[2:])
s = bin(int(input()))[2:]
ans = 0
for i in range(m):
    z = diff(L[i], s)
    if z <= k:
        ans += 1
print(ans)
