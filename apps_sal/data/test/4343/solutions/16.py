def main():
    n = int(input())
    s = [ord(c) - ord('a') for c in input()]
    t = [ord(c) - ord('a') for c in input()]
    r = [s[i] + t[i] for i in range(n)]
    for i in range(n - 1, 0, -1):
        if r[i] >= 26:
            r[i] -= 26
            r[i - 1] += 1
    k = 0
    rs = [0] * n
    for i in range(n):
        b = r[i] + k
        rs[i] = chr(b // 2 + ord('a'))
        if b % 2:
            k = 26
        else:
            k = 0
    return ''.join(rs)


print(main())
