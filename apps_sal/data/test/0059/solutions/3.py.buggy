n = int(input())
a = list(map(int, input().split()))
s = input()
sa = sorted(a)
h = {}
for i in range(n):
    h[sa[i]] = i
st = 0
for i in range(n):
    p = i
    ap = h[a[i]]
    if p - ap > st:
        print('NO')
        return
    if i < n - 1 and s[i] == '1':
        st += 1
    else:
        st = 0
st = 0
for i in range(n - 1, -1, -1):
    if i < n - 1 and s[i] == '1':
        st += 1
    else:
        st = 0
    p = i
    ap = h[a[i]]
    if ap - p > st + 1:
        print('NO')
        return

print('YES')
