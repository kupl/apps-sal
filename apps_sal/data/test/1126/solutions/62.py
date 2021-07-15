def main():
    n, x, m = list(map(int, input().split()))
    now = x
    l = [now]
    s = set([now])
    for i in range(n-1):
        now = now*now % m
        if now in s:
            break
        else:
            l.append(now)
            s.add(now)
    if n == len(l):
        print((sum(l)))
        return 0
    i = l.index(now)
    l1 = l[:i]
    l2 = l[i:]
    ans = sum(l1)
    n -= i
    size = len(l2)
    print((ans+((n//size)*sum(l2)+sum(l2[:n % size]))))


main()

