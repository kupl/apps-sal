def main():
    s = input()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            t = s[:i] + s[j:]
            if t == 'CODEFORCES':
                print('YES')
                return
    print('NO')
    return


main()
