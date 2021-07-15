def main():
    n, k = list(map(int, input().split()))
    if n == 0 or k == 0:
        print(0)
    else:
        s = str(n)
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                k -= 1
            else:
                res += 1
            if k == 0:
                break
        if k == 0:
            print(res)
        else:
            print(len(s)-1)

def __starting_point():
    main()

__starting_point()
