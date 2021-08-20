def main():
    (n, m) = list(map(int, input().split()))
    left = None
    right = None
    for _ in range(n):
        line = input().strip()
        cur_l = line.find('X')
        if cur_l != -1:
            if left is None:
                left = cur_l
            elif left != cur_l:
                print('NO')
                return
            cur_r = line.rfind('X')
            if right is None:
                right = cur_r
            elif right != cur_r:
                print('NO')
                return
            if '.' in line[cur_l:cur_r]:
                print('NO')
                return
    print('YES')


def __starting_point():
    main()


__starting_point()
