def main():
    a = input()
    l = len(a)
    book = [0] * 128
    a = list(a)
    for i in range(l):
        a[i] = chr(ord(a[i]) - ord('0'))
        book[ord(a[i])] += 1
    num = 0
    m = 0
    buf = []
    for i in range(1, 10):
        if i in (1, 8, 6, 9):
            for j in range(1, book[i]):
                buf.append(i)
                m = (10 * m + i) % 7
                num += 1
        else:
            for j in range(1, book[i] + 1):
                buf.append(i)
                m = (10 * m + i) % 7
                num += 1
    m = (m * 10000) % 7
    mp = [9681, 1896, 9861, 1698, 6891, 6981, 6819]
    buf.append(mp[m])
    num += 4
    buf.append('0' * (l - num))
    print(''.join(map(str, buf)))


main()
