def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            e = a[i][j]
            if e == 1:
                continue
            else:
                fl = False
                for i1 in range(n):
                    for j1 in range(n):
                        if a[i1][j] + a[i][j1] == e:
                            fl = True
                            break
                    if fl:
                        break
                if fl:
                    continue
                else:
                    print('No')
                    return
    print('Yes')

main()
