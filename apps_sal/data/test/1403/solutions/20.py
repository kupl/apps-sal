def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n, k = mi()
a = li()
a.sort()
ans = 0
i = 0
while i < len(a):
    j = i + 1
    c = 1
    while j < len(a) and a[j] <= a[j - 1] + k:
        if a[j] == a[j - 1]:
            c += 1
        else:
            c = 1
        j += 1
    ans += c
    i = j
print(ans)
