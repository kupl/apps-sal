def main():
    (s, k) = map(int, input().split())
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a[n - 1] < b[-m]:
        print('YES')
    else:
        print('NO')


main()
