# https://atcoder.jp/contests/abc155/submissions/10157837
# 写経

def main():
    a = [0]
    a += list(map(int, input()))
    a.reverse()

    n = len(a)
    b = a.copy()

    for i in range(n):
        if b[i] > 5 or (b[i] == 5 and b[i + 1] >= 5):
            b[i] = 0
            b[i + 1] += 1

    cnt = sum(b)
    for i in range(n):
        if a[i] > b[i]:
            b[i] += 10
            b[i + 1] -= 1
        cnt += b[i] - a[i]
    print(cnt)


def __starting_point():
    main()

__starting_point()
