n = int(input())
l = list(map(int, input().split()))
ans = 0
for elem in l:
    nn = 0
    ln = len(str(elem))
    for i in range(ln):
        nn += elem // 10 ** (ln - i - 1) % 10 * 11 * 10 ** ((ln - i - 1) * 2)
    ans += nn * n
print(ans % 998244353)
