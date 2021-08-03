def main():
    s = input()
    n = len(s)
    b = [1.0 / (i + 1) for i in range(n)]
    d = [(n - i) / (i + 1) for i in range(n)]
    d = d[::-1]
    for i in range(1, n):
        b[i] += b[i - 1]
        d[i] += d[i - 1]
    res = 0.0
    for i in range(n):
        if not(s[i] == 'I' or s[i] == 'E' or s[i] == 'A' or s[i] == 'O' or s[i] == 'U' or s[i] == 'Y'):
            continue
        z = [i + 1, n - i]
        z.sort()
        res += z[0] * (b[z[1] - 2] - b[z[0] - 1] + 1) + d[z[0] - 1]
    if len(s) == 1 and res > 0:
        res -= 1
    print(res)


main()
