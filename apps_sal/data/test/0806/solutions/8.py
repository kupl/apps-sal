from sys import stdin, stdout
prime = 10 ** 9 + 7


def unitMatrix(size):
    out = [[0] * size for i in range(size)]
    for i in range(size):
        out[i][i] = 1
    return out


def matrixMult(pre, post):
    rows = len(pre)
    mid = len(post)
    columns = len(post[0])
    out = [[0] * columns for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            for k in range(mid):
                out[i][j] += pre[i][k] * post[k][j]
                out[i][j] = out[i][j] % prime
    return out


def matrixExp(base, power):
    if power == 0:
        return unitMatrix(len(base))
    elif power % 2 == 0:
        half = matrixExp(base, power / 2)
        return matrixMult(half, half)
    else:
        half = matrixExp(base, (power - 1) / 2)
        return matrixMult(matrixMult(half, half), base)


def main():
    (n, l, r) = [int(i) for i in stdin.readline().split()]
    vals = [[1], [0], [0]]
    mods = [(r - l + 1) // 3, (r - l + 1) // 3, (r - l + 1) // 3]
    remainder = (r - l + 1) % 3
    if remainder >= 1:
        mods[l % 3] += 1
    if remainder == 2:
        mods[(l + 1) % 3] += 1
    transforms = [[mods[0], mods[2], mods[1]], [mods[1], mods[0], mods[2]], [mods[2], mods[1], mods[0]]]
    power = matrixExp(transforms, n)
    out = matrixMult(power, vals)
    print(out[0][0])


main()
