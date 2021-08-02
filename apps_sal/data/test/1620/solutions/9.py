import math


def main():
    n = int(input())
    ans = ""
    for i in range(n):
        if i % 4 == 0 or i % 4 == 1:
            ans += "a"
        else:
            ans += "b"
    print(ans)


main()
