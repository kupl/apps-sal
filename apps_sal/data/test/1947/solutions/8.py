n, m, l = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in a:
    if i > l:
        b.append(1)
    else:
        b.append(0)
ans = 0
i = 0
while i < n:
    if b[i]:
        ans += 1
        while i < n and b[i]:
            i += 1
    i += 1
for i in range(m):
    s = input()
    if s[0] == '0':
        print(ans)
    else:
        t, p, d = list(map(int, s.split()))
        if a[p - 1] <= l:
            a[p - 1] += d
            if a[p - 1] > l:
                b[p - 1] = 1
                if p - 2 >= 0 and b[p - 2] and p <= n - 1 and b[p]:
                    ans -= 1
                elif p - 2 >= 0 and b[p - 2] or p <= n - 1 and b[p]:
                    ans += 0
                else:
                    ans += 1
