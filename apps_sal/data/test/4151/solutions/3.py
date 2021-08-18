n = int(input())
a = [int(i) for i in input().split()]
s = list(set(a))
N = len(s)
d = {}
l = {}
for i in range(N):
    d[s[i]] = 0
    l[s[i]] = 0
for i in range(n):
    d[a[i]] += 1
ans = 0
cting = 0
for i in range(n):
    temp = d[a[i]]
    if temp > 1 and l[a[i]] == 0:
        l[a[i]] = 1
        cting += 1
        if cting == 1:
            ans += 1
        d[a[i]] -= 1

    elif l[a[i]] == 1:
        d[a[i]] -= 1
        if temp - 1 == 0:
            cting -= 1

    elif cting == 0:
        ans += 1

print(pow(2, ans - 1, 998244353))
