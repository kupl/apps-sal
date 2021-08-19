import collections


def main():
    n = int(input())
    s = input()
    a_list = []
    for i in range(n):
        if s[i] == 'W':
            a_list.append(0)
        else:
            a_list.append(1)
    r_count = sum(a_list)
    print(r_count - sum(a_list[0:r_count]))


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


def __starting_point():
    main()


__starting_point()
