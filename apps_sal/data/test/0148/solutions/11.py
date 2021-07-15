def main():
    n, a, x, b, y = list(map(int, input().split()))
    flag = False
    for i in range(n):
        if a == b:
            flag = True
        if a == x:
            break
        if b == y:
            break
        a += 1
        b -= 1
        if a == n + 1:
            a = 1
        if b == 0:
            b = n
    if flag:
        print('YES')
    else:
        print('NO')

main()

