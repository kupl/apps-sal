def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a == sorted(a):
        print('Yes')
        return
    tp = b[0]
    if (tp - 1) % 2 in b:
        print('Yes')
    else:
        print('No')


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
