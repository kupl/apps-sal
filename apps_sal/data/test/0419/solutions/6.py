def main():
    import sys
    input = sys.stdin.readline
    s = input()
    cnt = s.count('1')
    l = len(s) - 1
    if l & 1:
        if cnt > 1:
            print(l + 1 >> 1)
        else:
            print(l >> 1)
    else:
        print(l >> 1)
    return 0


main()
