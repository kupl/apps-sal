def main():
    (n, x) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = sum(a)
    print('YES' if s + (n - 1) == x else 'NO')


main()
