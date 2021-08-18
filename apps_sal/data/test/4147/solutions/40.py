N, A, B, C = list(map(int, input().split()))
L = []
for _ in range(N):
    L.append(int(input()))


def test(n, a, b, c, na, nb, nc):
    """
    :param n: 使用している竹の本数
    :param a: 竹aの長さ
    :param b: 竹bの長さ
    :param c: 竹cの長さ
    :param na: 竹aに使用した本数
    :param nb: 竹bに使用した本数
    :param nc: 竹cに使用した本数
    :return: 消費MP
    """
    if n == N:
        if min(na, nb, nc) == 0:
            return 10**9
        else:
            mp = 0
            mp += (na - 1) * 10 if na else 0
            mp += (nb - 1) * 10 if nb else 0
            mp += (nc - 1) * 10 if nc else 0
            mp += abs(A - a) + abs(B - b) + abs(C - c)
            return mp
    else:
        mp1 = test(n + 1, a, b, c, na, nb, nc)
        mp2 = test(n + 1, a + L[n], b, c, na + 1, nb, nc)
        mp3 = test(n + 1, a, b + L[n], c, na, nb + 1, nc)
        mp4 = test(n + 1, a, b, c + L[n], na, nb, nc + 1)
        return min(mp1, mp2, mp3, mp4)


print((test(0, 0, 0, 0, 0, 0, 0)))
