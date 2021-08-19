def main():
    (n, m) = map(int, input().split())
    mas = list(map(int, input().split()))
    mas.sort()
    mas.append(int(1000000000.0))
    ans = 0
    res = []
    ind = 0
    for i in range(1, int(1000000000.0)):
        if m < i:
            break
        if mas[ind] == i:
            ind += 1
        else:
            ans += 1
            m -= i
            res.append(i)
    print(ans)
    print(*res)


main()
