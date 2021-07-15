def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mod = 10 ** 9+ 7
    ans = 1

    def answer(a):
        ans =1
        for x in a:
            ans *= x
            ans %= mod
        return ans

    if n == k:
        print(answer(a))
        return
    a.sort(reverse=True, key= lambda x:abs(x))
    if sum(x<0 for x in a[:k])%2 == 0:
        print(answer(a[:k]))
    else:
        if all(x < 0 for x in a):
            print(answer(a[-k:]))
        else:
            try:
                x1, y1= min([x for x in a[:k] if x > 0]), min([x for x in a[k:] if x < 0])
            except ValueError:
                x1, y1 = 1, 0
            try:
                x2, y2= max([x for x in a[:k] if x < 0]),\
                    max([x for x in a[k:] if x >= 0])
            except ValueError:
                x2, y2 = 1, 0
            if abs(x2*y1) > abs(x1*y2):           
                a[a.index(x1)] = y1
            else:
                a[a.index(x2)] = y2
            print(answer(a[:k]))
            


def __starting_point():
    main()
__starting_point()
