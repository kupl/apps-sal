n, k = [int(_) for _ in input().split()]
a = input()
k += 1
# size of n+1
f = [0] * (n + 1)

f[1] = int(a[0] == '0')
for i in range(1, n + 1):
    f[i] = f[i - 1] + int(a[i - 1] == '0')

# sprint(f)


def check(dis):
    for i in range(n):
        if a[i] == '0':
            left = max(i - dis, 0)
            right = min(i + dis, n - 1)
            if f[right + 1] - f[left] >= k:
                return True
    return False


l = 1
r = n
ans = n
while l <= r:
    mid = (l + r) // 2
    # print(mid)
    if check(mid):
        # print(True)
        ans = min(ans, mid)
        r = mid - 1

    else:
        # print(False)
        l = mid + 1
print(ans)
