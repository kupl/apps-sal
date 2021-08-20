def main():
    s = input()
    a = ''
    for i in s:
        if i != 'a':
            a += i
    if len(a) & 1:
        print(':(')
        return 0
    n = len(a) >> 1
    A = a[:n]
    B = a[n:]
    if A != B:
        print(':(')
        return 0
    N = len(s)
    if s[N - n:] == A:
        print(s[:N - n])
        return 0
    else:
        print(':(')
        return 0


main()
