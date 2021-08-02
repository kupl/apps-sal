n = int(input())
a = list(map(int, input().split()))
b = a[:]
s = set()
for i in range(n):
    if(a[i] in s):
        a[i] = 0
    else:
        s.add(a[i])
s = set()
c = [0] * n
c[n - 1] = 1
for i in range(n - 1, -1, -1):
    if(b[i] in s):
        b[i] = 0
        c[i] = c[i + 1]
    else:
        s.add(b[i])
        if(i < n - 1):
            c[i] = c[i + 1] + 1
ans = 0
for i in range(n - 1):
    if(a[i]):
        ans += c[i + 1]
print(ans)
