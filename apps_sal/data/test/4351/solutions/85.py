
url = "https://atcoder.jp//contests/abc070/tasks/abc070_a"

def main():
    x = input()
    if x == ''.join(reversed(x)):
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()

__starting_point()
