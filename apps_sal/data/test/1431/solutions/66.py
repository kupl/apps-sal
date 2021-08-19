n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] * (n + 1)
for i in reversed(list(range(1, n + 1))):
    ans = 0
    for j in range(i, n + 1, i):
        ans += b[j]
    if ans % 2 == a[i]:
        b[i] = 0
    else:
        b[i] = 1
c_ = []
for (c, d) in enumerate(b):
    if d == 1:
        c_.append(str(c))
print(len(c_))
print(' '.join(c_))
