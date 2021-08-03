n = int(input())
a = list(map(int, input().split()))
a_ = sum(a)
b = 0
for i in range(1, n, 2):
    b += 2 * a[i]
ans = a_ - b
c = []
c.append(str(ans))
for i in range(n - 1):
    ans = 2 * a[i] - ans
    c.append(str(ans))
print((' '.join(c)))
