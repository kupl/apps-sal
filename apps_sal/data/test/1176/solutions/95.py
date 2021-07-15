def main():
    n = int(input())
    a = list(map(int, input().split()))
    s, cnt = [0]*n, 0
    for i in range(n):
        s[i] = abs(a[i])
        if a[i] < 0:
            cnt += 1
    if cnt%2:
        print(sum(s) - 2*min(s))
    else:
        print(sum(s))

def __starting_point():
    main()
__starting_point()
