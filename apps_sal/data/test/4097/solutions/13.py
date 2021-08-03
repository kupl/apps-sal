m = [0, -1, 1]


def solve(b):
    n = len(b)
    if n < 3:
        return 0
    minans = -1
    for ii in range(3):
        for jj in range(3):
            b1 = b[0] + m[ii]
            bn = b[n - 1] + m[jj]
            dn = bn - b1
            if dn % (n - 1) == 0:
                d = dn // (n - 1)
                currans = 0
                for i in range(n):
                    if b[i] == b1 + i * d:
                        pass
                    elif abs(b[i] - (b1 + i * d)) == 1:
                        currans += 1
                    else:
                        currans = -1
                        break
                if minans == -1 or currans != -1 and currans < minans:
                    minans = currans
    return minans


n = int(input())
b = [int(s) for s in input().split()]

print(solve(b))
