def main():
    n,a,x,b,y = list(map(int,input().split()))
    same = False
    while True:
        if a != x:
            a += 1
        else:
            break
        if b != y:
            b -= 1
        else:
            break
        if a == n+1:
            a = 1
        if b == 0:
            b = n

        if a == b:
            break

    if a == b:
        print('YES')
    else:
        print('NO')


main()

