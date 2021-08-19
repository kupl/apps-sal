# https://codeforces.com/contest/1166/problem/D
def creat_r(X, k, m, p):
    q = X // p[k]
    r = X % p[k]

    R = []
    for _ in range(k + 1):
        R.append(q)

    s = bin(r)[2:]
    for i in range(1, len(s) + 1):
        if s[-i] == '1':
            R[-(i + 1)] += 1

    return R


i = 1
p = [1]
for _ in range(50):
    i *= 2
    p.append(i)

T = int(input())
ans = []
for _ in range(T):
    a, b, m = map(int, input().split())
    if a == b:
        print(1, a)
        continue

    flg = False
    for i in range(50):
        if p[i] * a >= b:
            break

        k = i
        X = b - (p[i] * a)

        if X >= p[k] and X <= p[k] * m:
            flg = True
            R = creat_r(X, k, m, p)
            sR = 0
            A = [a]

            for _ in range(k + 1):
                A.append(p[_] * a + sR + R[_])
                sR += sR + R[_]

            print(len(A), end=' ')
            for x in A:
                print(x, end=' ')
            print()
            break

    if flg == False:
        print(-1)
