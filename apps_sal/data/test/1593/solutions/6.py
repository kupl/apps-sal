__author__ = 'Lipen'


def main():
    (n, s) = map(int, input().split())
    data = []
    for _ in range(n):
        (x, y, k) = map(int, input().split())
        r = pow(x, 2) + pow(y, 2)
        data.append([x, y, k, r])
    rmin = -1
    for i in range(n):
        count = 0
        r = data[i][3]
        for j in range(n):
            if data[j][3] <= r:
                count += data[j][2]
        if count + s >= 1000000 and (r < rmin or rmin == -1):
            rmin = r
    if rmin == -1:
        print(-1)
    else:
        print(pow(rmin, 0.5))


main()
