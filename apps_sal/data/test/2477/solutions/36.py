def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    def value(v):
        cnt = 0
        for i in a:
            cnt += (i-1)//v
        if cnt > k:
            return False
        else:
            return True

    def b_search(ok, ng, value):
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if value(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print((b_search(10**16, 0, value)))


main()

