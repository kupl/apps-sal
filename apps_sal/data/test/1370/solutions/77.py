from itertools import accumulate


def solve(h, w, lim, choco):
    acc = [[0] + list(accumulate((int(c == '1') for c in s))) for s in choco]
    acc = list(zip(*acc))
    acc = [[0] + list(accumulate(s)) for s in acc]
    acc = list(zip(*acc))
    ans = 10 ** 9
    for bit in range(1 << h - 1):
        k = 1
        tmp = 0
        while k < w:
            i = 0
            l = w + 1
            sp = bit | 1 << h - 1
            while sp:
                b = sp & -sp
                sp ^= b
                j = b.bit_length()
                lt = k
                while lt <= w and acc[j][lt] - acc[j][k - 1] - acc[i][lt] + acc[i][k - 1] <= lim:
                    lt += 1
                if lt == k:
                    break
                l = min(l, lt)
                i = j
            else:
                k = l
                if k <= w:
                    tmp += 1
                continue
            break
        else:
            ans = min(ans, tmp + bin(bit).count('1'))
    return ans


(h, w, k) = list(map(int, input().split()))
choco = [input() for _ in range(h)]
print(solve(h, w, k, choco))
