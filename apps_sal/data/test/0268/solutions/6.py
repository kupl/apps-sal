from bisect import bisect


def main():
    n, k, d = list(map(int, input().split()))
    if k == 1:
        print('YES')
        return
    l = []
    ll = [l]
    a = 10 ** 10
    for b in sorted(map(int, input().split())):
        if a < b:
            if len(l) < k:
                print('NO')
                return
            l = [b]
            ll.append(l)
        else:
            l.append(b)
        a = b + d

    def f(a):
        def dfs(i):
            avail[i] = False
            if i + k <= le:
                if a[-1] <= a[i] + d:
                    raise TabError
                j = bisect(a, a[i] + d, i, -1) - 1
                for j in range(bisect(a, a[i] + d, i, -1), i + k - 1, -1):
                    if avail[j]:
                        dfs(j)

        le = len(a)
        avail = [True] * le
        try:
            dfs(0)
        except TabError:
            return True
        return False

    print(('NO', 'YES')[all(map(f, ll))])


def __starting_point():
    main()


__starting_point()
