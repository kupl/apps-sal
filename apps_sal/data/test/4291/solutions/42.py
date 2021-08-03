n, q = list(map(int, input().split()))
#print(n, q)

s = input()

v = [0] * n

for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        v[i] = 1

m = [0] * (n + 1)
for i in range(n):
    m[i + 1] = m[i] + v[i]


for i in range(q):
    l, r = list(map(int, input().split()))
    l -= 1
    ans = 0
    if r - l < 2:
        ans = 1
    else:
        ans = m[r] - m[l]
        if v[r - 1] == 1:
            ans -= 1
    print(ans)
