def process_moves(v, moves, n):
    update = True
    for m in moves:
        if update:
            bit_pos = 0
            t = v
            while t > 0:
                if t & 1 == 1:
                    break
                t >>= 1
                bit_pos += 1

            power_of_2 = t == 1

        if m == 'U':
            if power_of_2:
                new_v = v << 1
            else:
                new_v = v & ~(1 << bit_pos) | (1 << (bit_pos + 1))
        elif m == 'L':
            if power_of_2:
                new_v = v >> 1
            else:
                if bit_pos > 0:
                    new_v = v & ~(1 << bit_pos) | (1 << (bit_pos - 1))
                else:
                    new_v = 0
        else:  # m == 'R'
            if bit_pos > 0:
                new_v = v | (1 << (bit_pos - 1))
            else:
                new_v = 0

        if 1 <= new_v <= n:
            update = True
            v = new_v

    return v


def main():
    n, q = list(map(int, input().split()))
    for i in range(q):
        s = int(input())
        moves = input()
        print(process_moves(s, moves, n))


def __starting_point():
    # import sys
    # sys.stdin = open("D.txt")
    main()

__starting_point()
