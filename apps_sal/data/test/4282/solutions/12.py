def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
if n == 3:
    ans = [1, 2, 3]
else:
    a = [None] + [li() for i in range(n)]
    ans = []
    i = 1
    while 1:
        ans.append(i)
        j = a[i][0]
        if a[i][1] not in a[j]:
            j = a[i][1]
        i = j
        if i == 1:
            break
print(*ans)
