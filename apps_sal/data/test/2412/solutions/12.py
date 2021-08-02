def solve():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == '8':
            break
    if i <= n - 11:
        print("YES")
    else:
        print("NO")


def main():
    for _ in range(int(input())):
        solve()
    return 0


main()
