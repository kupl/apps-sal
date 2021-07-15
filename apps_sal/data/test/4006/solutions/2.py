def main():
    s = set()
    n = int(input())
    def f(x):
        x += 1
        while not x % 10:
            x //= 10
        return x
    while n not in s:
        s.add(n)
        n = f(n)
    print(len(s))
    return 0

main()
