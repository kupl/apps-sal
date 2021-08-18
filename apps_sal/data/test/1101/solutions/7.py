n, k = [int(_) for _ in input().split()]
a = input()

k += 1
f = [0] * (n + 1)

f[1] = int(a[0] == '0')
for i in range(2, n + 1):
    f[i] = f[i - 1] + int(a[i - 1] == '0')


def check(dis):
    for i in range(n):
        if a[i] == '0':
            left = max(i - dis, 0)
            right = min(i + dis, n - 1)
            total = f[right + 1] - f[left]
            if total >= k:
                return True
    return False


l = 1
r = n - 1
while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)
