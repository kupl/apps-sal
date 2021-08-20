def main():
    n = int(input())
    s = input()
    l = -1
    r = -1
    for i in range(n - 1):
        if ord(s[i + 1]) < ord(s[i]):
            l = i + 1
            r = i + 2
            break
    if l != -1 and r != -1:
        print('YES')
        print(l, r)
    else:
        print('NO')


main()
