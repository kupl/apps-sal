n = int(input())
a = list(map(int, input().split()))
b = []
c = []
ans = 0
for i in range(n):
    b.append(i + 1 - a[i])
    c.append(a[i] + i + 1)
x = max(b)
if x <= 0:
    print(0)
    return
else:
    ans = 0
    b_ = [0] * (x + 1)
    for i in range(n):
        if 0 <= b[i] <= x:
            b_[b[i]] += 1
    for i in range(n):
        if 0 <= c[i] <= x:
            ans += b_[c[i]]
    print(ans)
