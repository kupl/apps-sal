def main():
    (a, b) = map(int, input().split())
    if abs(a - b) <= 1 and (a != 0 or b != 0):
        print('YES')
    else:
        print('NO')


main()
