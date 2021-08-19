(N, K) = map(int, input().split())
(R, S, P) = map(int, input().split())
T = input()


def janken(n):
    if n == 'r':
        return P
    elif n == 's':
        return R
    else:
        return S


ans = 0
for i in range(K):
    h = T[i::K]
    l = len(h)
    f = 1
    a = ''
    for j in range(l):
        if a != h[j]:
            a = h[j]
            f = 0
            ans += janken(h[j])
        else:
            ans += f * janken(h[j])
            f = -(f - 1)
print(ans)
