def main():
    n = int(input())
    n = hex(n)[2:]
    ans = 0
    for c in n:
        if c == '0' or c == '6' or c == '9' or c == 'a' or c == 'd' or c == '4':
            ans += 1
        if c == '8' or c == 'b':
            ans += 2
    print(ans)

def __starting_point():
    main()

__starting_point()
