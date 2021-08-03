def main():
    c = list(map(int, input().split()))
    s = sum(c)
    for i in range(2**4):
        tmp = 0
        for j in range(4):
            if i >> j & 1:
                tmp += c[j]
        if tmp == s - tmp:
            print('Yes')
            break
    else:
        print('No')


main()
