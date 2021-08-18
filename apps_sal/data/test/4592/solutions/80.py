N = int(input())
p = 10**9 + 7


def primeryNum(n):
    n_ = int(n**0.5)
    ary = list(range(n + 1))
    ary[1] = 0
    for a in ary:
        if a > n_:
            break
        elif a == 0:
            continue

        for i in range(a * 2, n + 1, a):
            ary[i] = 0
    return ary


primeryN = primeryNum(N)

divN = [0] * (N + 1)
for pn in primeryN:
    if pn == 0:
        continue
    i = 1
    cnt = 0
    while (pn**i <= N):
        cnt += (N // pn**i)
        i += 1
    divN[pn] = cnt

ans = 1
for d in divN:
    if d == 0:
        continue
    ans = (ans * (d + 1)) % p
print(ans)
