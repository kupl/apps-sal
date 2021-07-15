def main():
    from sys import stdin, stdout
    input = stdin.readline
    print = stdout.write
    for _ in range(int(input())):
        ans = 0
        i = -1
        s = input()
        for j in range(len(s) - 1):
            if s[j] == '1':
                c = 0
                for k in range(j, len(s)):
                    c = c * 2 + (s[k] == '1') + (s[k] == '\n') * k
                    if k - i < c:
                        ans += k - j
                        break
                i = j
        print(f'{ans}\n')


main()

