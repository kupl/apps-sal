def main():
    k = int(input())
    s = list(input())
    n = len(s)
    d = [0] * 10
    for i in range(n):
        d[int(s[i])] += 1
    a = 0
    for i in range(10):
        a += i * d[i]
    if k <= a:
        print(0)
        return
    i = 0
    c = 0
    while k > a:
        if d[i] == 0:
            i += 1
            continue
        a += 9 - i
        d[i] -= 1
        c += 1
    print(c)


main()
