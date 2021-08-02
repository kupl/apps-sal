def main(N, lines):
    a = sorted([line[0] for line in lines])
    b = sorted([line[1] for line in lines])

    if N % 2 == 1:
        mi = a[N // 2]
        ma = b[N // 2]
        print((int(ma - mi + 1)))
    else:
        mi = (a[N // 2 - 1] + a[N // 2])
        ma = (b[N // 2 - 1] + b[N // 2])
        print((int(ma - mi + 1)))


N = int(input())
lines = []
for i in range(N):
    lines.append(list(map(int, input().split())))
main(N, lines)
