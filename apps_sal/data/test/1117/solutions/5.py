def main():
    n = int(input())
    if n == 1:
        print('YES')
        return 0
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    c = 0
    if max(lst[0]) < min(lst[1]):
        print('NO')
        return 0
    for i in range(1, n + 1):
        if min(lst[-i]) >= c:
            c = min(lst[-i])
        elif max(lst[-i]) >= c:
            c = max(lst[-i])
        else:
            print('NO')
            return 0
    print('YES')
    return 0


main()
