import collections
url = "https://atcoder.jp//contests/abc111/tasks/arc103_a"


def main():
    input()
    t = list(map(int, input().split()))
    even_lis = t[::2]
    odd_lis = t[1::2]
    e = collections.Counter(even_lis).most_common()
    odd = collections.Counter(odd_lis).most_common()
    if e[0][0] == odd[0][0]:
        if e[0][1] + odd[0][1] == len(t):
            print((e[0][1]))
            return
        else:
            print((len(t) - max(e[0][1], odd[0][1]) - max(e[1][1], odd[1][1])))
            return
    else:
        print((len(t) - e[0][1] - odd[0][1]))


def __starting_point():
    main()


__starting_point()
