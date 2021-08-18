

def main():
    try:
        while True:
            n, k = list(map(int, input().split()))
            ls = sorted((input() for i in range(n)), key=len)
            true = len(input())
            first = 1e9
            last = 0
            cur = 0
            flag = True
            for i, s in enumerate(ls):
                cur += 1
                if len(s) == true:
                    last = cur
                    if flag:
                        flag = False
                        first = cur
                elif not flag:
                    break
                if (i + 1) % k == 0:
                    cur += 5

            print(first, last)

    except EOFError:
        pass


main()
