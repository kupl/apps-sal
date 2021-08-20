def jan(x, a, b, c):
    if x == 's':
        return a
    elif x == 'r':
        return c
    else:
        return b


(n, k) = map(int, input().split())
(r, s, p) = map(int, input().split())
r = int(r)
s = int(s)
p = int(p)
t = list(input())
m = [0] * n
ans = 0
for i in range(n):
    if i >= k:
        if t[i] == t[i - k]:
            if m[i - k] == 1:
                ans += jan(t[i], r, s, p)
            else:
                m[i] = 1
        else:
            ans += jan(t[i], r, s, p)
    else:
        ans += jan(t[i], r, s, p)
print(ans)
