def main():
    (n, m) = map(int, input().split())
    l = list(map(int, input().split()))
    a = [0 for i in range(n)]
    for i in range(m - 1):
        d = l[i + 1] - l[i]
        if d <= 0:
            d += n
        if a[l[i] - 1] == 0:
            a[l[i] - 1] = d
        elif a[l[i] - 1] != d:
            return -1
    cnt = [0 for i in range(n + 1)]
    for i in a:
        cnt[i] += 1
    unused = set()
    for i in range(1, n + 1):
        if cnt[i] == 0:
            unused.add(i)
        elif cnt[i] > 1:
            return -1
    for i in range(n):
        if a[i] == 0:
            a[i] = unused.pop()
    return ' '.join(map(str, a))


print(main())
