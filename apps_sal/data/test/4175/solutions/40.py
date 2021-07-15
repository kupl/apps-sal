def check_shiritori(n:int, w:list)->bool:
    if len(set(w)) < n:
        return False
    for i in range(n - 1):
        if w[i][-1] != w[i + 1][0]:
            return False
    return True


def main():
    n = int(input())
    w = []
    for i in range(n):
        w.append(input())

    if check_shiritori(n, w):
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()

__starting_point()
