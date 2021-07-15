n = int(input())
a = list(map(int,input().split()))
rev = [-1] * (n + 1)
for i, j in enumerate(a):
    rev[j] = i

mx = max(a)

# [l, r]
l = a.index(mx)
r = l

for i in range(n - 1, 0, -1):
    idx = rev[i]
    if idx == l - 1:
        l -= 1
    elif idx == r + 1:
        r += 1
    else:
        print('NO')
        return
print('YES')
