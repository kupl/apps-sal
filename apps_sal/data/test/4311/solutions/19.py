def main():
    def f(n):
        return 3 * n + 1 if n % 2 else n // 2
    s = int(input())
    a = [s]
    for i in range(1, 11**6):
        x = f(a[i - 1])
        if x in a:
            return len(a) + 1
            return
        a.append(x)


print(main())
