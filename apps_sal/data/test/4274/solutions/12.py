from sys import stdin


def nii():
    return map(int, stdin.readline().split())


def lnii():
    return list(map(int, stdin.readline().split()))


(n, m) = nii()
print('Yes' if n == m else 'No')
