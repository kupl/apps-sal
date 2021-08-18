n, k = map(int, input().split())
A = list(map(int, input().split()))


a = [0]
for i in range(n):
    a.append(a[i] + A[i])


def is_ok(tmp, arg):
    return a[arg] - a[tmp] >= k


cnt = 0
for i in range(n):
    top, bot = n + 1, i
    while top - bot > 1:
        mid = (top + bot) // 2
        if is_ok(i, mid):
            top = mid
        else:
            bot = mid
    cnt += n - top + 1

print(cnt)
