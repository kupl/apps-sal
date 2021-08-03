n, m = map(int, input().split())
a1 = 0
ans = 1
for i in range(m + 1):
    if i == m:
        a2 = n + 1
    else:
        a2 = int(input())
    l = a2 - a1
    if l == 0:
        print(0)
        return
    if l > 2:
        fst = 1
        snd = 1
        for _ in range(l - 2):
            nfst = snd
            snd = fst + nfst
            fst = nfst
        ans *= snd
    a1 = a2 + 1
print(ans % (10**9 + 7))
