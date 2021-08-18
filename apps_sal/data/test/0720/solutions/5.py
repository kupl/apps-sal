

def main():
    n = int(input())
    pre_a, pre_b, ret = 0, 0, 1
    for _ in range(n):
        curr_a, curr_b = map(int, input().split())
        if pre_a == pre_b:
            ret += min(curr_a, curr_b) - pre_a
        else:
            ret += max(0, min(curr_a, curr_b) - max(pre_a, pre_b) + 1)
        pre_a, pre_b = curr_a, curr_b
    print(ret)


def __starting_point():
    main()


__starting_point()
