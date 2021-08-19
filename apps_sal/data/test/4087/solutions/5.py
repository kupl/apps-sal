def main():

    def is_interesting(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        if s % 4 == 0:
            return 1
        return 0
    import sys
    input = sys.stdin.readline
    a = int(input())
    while not is_interesting(a):
        a += 1
    print(a)
    return 0


main()
