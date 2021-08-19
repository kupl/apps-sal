def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        (a, b) = list(map(int, input().split()))
        if a == b:
            cnt += 1
        else:
            cnt = 0
        if cnt > 2:
            print('Yes')
            return 0
    print('No')


main()
