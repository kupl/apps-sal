n = int(input())
s = list(input())
c = list(map(int, input().split()))
h = a = r = d = 0
for i in range(n):
    if s[i] == 'h':
        h += c[i]
    elif s[i] == 'a':
        a = min(h, a + c[i])
    elif s[i] == 'r':
        r = min(a, r + c[i])
    elif s[i] == 'd':
        d = min(r, d + c[i])
print(d)
