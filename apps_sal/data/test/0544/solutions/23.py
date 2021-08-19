l = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
for i in range(int(input())):
    n = int(input())
    s = input()
    if s == s[::-1]:
        print('YES')
    else:
        f = 1
        for i in range(n // 2):
            if abs(l[s[i]] - l[s[n - i - 1]]) != 2 and abs(l[s[i]] - l[s[n - i - 1]]) != 0:
                f = 0
        if f:
            print('YES')
        else:
            print('NO')
