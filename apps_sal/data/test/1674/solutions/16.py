(n, m) = list(map(int, input().split()))
a = list(map(int, input().split())) + [1]
s = input() + '0'
last = '1'
l = [0]
ans = 0
for i in range(n + 1):
    if last != s[i]:
        l.sort()
        if len(l) < m:
            ans += sum(l)
        else:
            ans += sum(l[len(l) - m:])
        l.clear()
    l.append(a[i])
    last = s[i]
print(ans)
