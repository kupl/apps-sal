3
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(0, n):
    if k == 0 or a[i] >= 0:
        break
    a[i] *= -1
    k -= 1
a.sort()
if k % 2 == 0 or 0 in a:
    print(sum(a))
else:
    print(sum(a) - 2 * a[0])
