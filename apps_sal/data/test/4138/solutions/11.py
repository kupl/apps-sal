def init(maxn):
    Sum = [0] * maxn
    Single = [0] * maxn
    for i in range(1, maxn):
        lens = 10 ** i - 10 ** (i - 1)
        pre = Single[i - 1]
        Single[i] = pre + lens * i
    for i in range(1, maxn):
        lens = 10 ** i - 10 ** (i - 1)
        pre = Single[i-1]
        Sum[i] = (pre + i + pre + lens * i) * lens // 2 + Sum[i - 1]
    return Sum, Single

def getAns(n, Sum, Single, maxn):
    ans = 0
    minn = n
    index = 0
    L, R = 1, 10 ** maxn
    while L <= R:
        m = (L + R) // 2
        digit = len(str(m))
        lens = m - 10 ** (digit - 1) + 1
        pre = Single[digit - 1]
        cnt = (pre + digit + pre + lens * digit) * lens // 2 + Sum[digit - 1]
        if cnt < n:
            index = m
            minn = min(minn, n - cnt)
            L = m + 1
        else :
            R = m - 1
    #print(index, minn)
    n = minn
    L, R = 1, index + 11
    index = 0
    while L <= R:
        m = (L + R) // 2
        digit = len(str(m)) 
        lens = m - 10 ** (digit - 1) + 1
        pre = Single[digit - 1]
        cnt = pre + lens * digit
        if cnt < n:
            index = m
            minn = min(minn, n - cnt)
            L = m + 1
        else :
            R = m - 1
    return str(index + 1)[minn - 1]

def test():
    ans = 0
    Sum = 0
    for i in range(1, 1000):
        ans += len(str(i))
        Sum += ans
        if i % 10 == 9:
            print(i, ans, Sum)


def main():
    maxn = 10
    Sum, Single = init(maxn)
    T = int(input())
    for i in range(T):
        n = int(input())
        print(getAns(n, Sum, Single, maxn))

    

def __starting_point():
    main()
__starting_point()
