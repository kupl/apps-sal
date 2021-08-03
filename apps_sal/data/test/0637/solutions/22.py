def main():
    n = int(input())
    photo = [int(x) for x in (input().split())]
    color = dict()
    cnt = 0
    for i in range(n):
        if i == 0:
            cnt += 1
            continue
        if photo[i] == photo[i - 1]:
            cnt += 1
        if photo[i] != photo[i - 1]:
            color[cnt] = 1
            cnt = 1
        if i == n - 1:
            color[cnt] = 1
    if len(color) <= 1:
        print('YES')
    else:
        print('NO')


main()
