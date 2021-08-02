def main():
    n = int(input())
    a = input()
    if n == 1:
        print('Yes')
        return
    c = [0] * 300
    for i in a:
        if c[ord(i)] > 0:
            print('Yes')
            return
        c[ord(i)] += 1
    print('No')


main()
