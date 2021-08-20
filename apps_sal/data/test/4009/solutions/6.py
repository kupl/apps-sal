def main():
    (n, x, y) = map(int, input().split())
    s = input()
    ans = 0
    for i in range(-1, -x - 1, -1):
        if i == -(y + 1):
            ans += s[i] != '1'
            continue
        ans += s[i] == '1'
    print(int(ans))
    return 0


main()
