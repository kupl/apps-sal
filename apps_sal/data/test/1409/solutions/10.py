__author__ = 'Lipen'


def main():
    (n, k) = map(int, input().split())
    ydata = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n // 3):
        d = ydata[i * 3:(i + 1) * 3]
        if d[0] <= 5 - k and d[1] <= 5 - k and (d[2] <= 5 - k):
            ans += 1
        else:
            break
    print(ans)


main()
