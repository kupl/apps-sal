
url = "https://atcoder.jp//contests/abc120/tasks/abc120_a"

def main():
    a, b, c = list(map(int, input().split()))
    ans = b // a
    print(ans) if c >= ans else print(c)

def __starting_point():
    main()

__starting_point()
