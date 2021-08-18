def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) == m:
        print('YES')
    else:
        print('NO')


rw = int(input())
for wewq in range(rw):
    main()
