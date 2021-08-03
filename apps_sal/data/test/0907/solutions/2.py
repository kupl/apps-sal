def main():
    def check(x, y):
        for a, b in mas:
            if not((a == x or a == y) or (b == x or b == y)):
                return [a, b]
        return [-1, -1]

    def check1(x, y):
        for a, b in mas:
            if not((a == x or a == y) or (b == x or b == y)):
                return False
        return True
    n, m = list(map(int, input().split()))
    mas = []
    ans = False
    for i in range(m):
        mas.append(sorted(list(map(int, input().split()))))
    k = check(*mas[0])
    if k == [-1, -1]:
        print('YES')
    else:
        ans = check1(mas[0][0], k[0]) or check1(mas[0][0], k[1]) or check1(mas[0][1], k[0]) or check1(mas[0][1], k[1])
        if ans:
            print('YES')
        else:
            print('NO')


main()
