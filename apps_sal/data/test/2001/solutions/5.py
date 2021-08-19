import sys
input = sys.stdin.readline
out = sys.stdout
MOD = 1000000007


def main():
    (n, q) = list(map(int, input().split()))
    s = input()
    d = {}
    count_1 = 0
    count_0 = 0
    for i in range(n):
        if s[i] == '1':
            count_1 += 1
        else:
            count_0 += 1
        z = (count_1, count_0)
        d[i] = z
    for i in range(q):
        (li, ri) = list(map(int, input().split()))
        li -= 1
        ri -= 1
        if li == 0:
            answer = (pow(2, d[ri][0], MOD) - 1) * pow(2, d[ri][1], MOD)
        else:
            answer = (pow(2, d[ri][0] - d[li - 1][0], MOD) - 1) * pow(2, d[ri][1] - d[li - 1][1], MOD)
        out.write(str(answer % MOD) + '\n')


def __starting_point():
    main()


__starting_point()
