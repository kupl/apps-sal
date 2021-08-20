def main():
    n = int(input())
    line = input()
    turn_take = []
    prev = line[-1]
    can_be = 0
    for i in range(n - 2, -1, -1):
        if line[i] == prev:
            can_be += 1
        else:
            prev = line[i]
            turn_take.append(can_be)
    turn_take.append(can_be)
    turns = len(turn_take)
    taken = 0
    res = 0
    for i in range(1, turns + 1):
        if i > 1 and turn_take[-i] < turn_take[-i + 1]:
            taken = min(0, taken + turn_take[-i + 1] - turn_take[-i])
        if turn_take[-i] > -taken:
            taken -= 1
            res += 1
        else:
            res += (turns - i + 1) // 2
            if (turns - i + 1) % 2 != 0:
                res += 1
            break
    print(res)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


'\n1 2 3 4 5\n1 2 4 4\n1 2 4\n1 3\n2\n1 2 3 4 5 6\n1 2 3 5 5\n1 2 3 5\n1 2 4\n1 3\n2\n1 2 3 4 5 6 7 ( max, max - 2)\n1 2 3 4 6 6 (max - 1, max - 1)\n1 2 3 4 6 (max - 1, max - 3)\n1 2 3 5 (max - 2 max - 4)\n1 2 4\n1 3\n2\n1 2 3 4 5 6 7 8 (6, 8)\n1 2 3 4 5 7 7 (7, 7)\n1 2 3 4 5 7 (5, 7)\n1 2 3 4 6 (4, 6)\n1 2 3 5 (3, 5)\n1 2 4 (2, 4)\n1 3 (1, 3)\n2\n'
__starting_point()
