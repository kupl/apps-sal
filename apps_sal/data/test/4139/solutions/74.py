import itertools


def main():
    n = int(input())
    tar_list = []
    cnt = 0

    for a in range(3, len(str(n)) + 1):
        target = list(itertools.product([3, 5, 7], repeat=a))
        for tar in target:
            tar_list = list(tar)
            if tar.count(3) > 0 and tar.count(5) > 0 and tar.count(7):
                ans = 0
                i = a - 1
                for ii in tar_list:
                    ans += ii * (10**i)
                    i -= 1
                if ans <= n:
                    cnt += 1

    print(cnt)


def __starting_point():
    main()


__starting_point()
