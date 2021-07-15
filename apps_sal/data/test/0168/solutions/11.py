def main():
    n = int(input())
    s = input()
    mi = 0
    c = 0
    for i in s:
        if i == '+':
            c += 1
        else:
            c -= 1
        mi = min(mi, c)
    print(c - mi)
    return 0
main()
