from sys import stdin, stdout
MOD = 10 ** 9 + 7


def find(arr, N):
    R = [0, 0, 0]
    Z = 1
    for i in arr:
        if i == 'a':
            R[0] += Z
        if i == 'b':
            R[1] = (R[1] + R[0]) % MOD
        if i == 'c':
            R[2] = (R[2] + R[1]) % MOD
        if i == '?':
            (a, b, c) = (R[:], R[:], R[:])
            a[0] = (a[0] + Z) % MOD
            b[1] = (b[1] + b[0]) % MOD
            c[2] = (c[2] + c[1]) % MOD
            R = [(a[i] + b[i] + c[i]) % MOD for i in range(3)]
            Z = Z * 3 % MOD
    return R[2] % MOD


def main():
    N = int(stdin.readline())
    arr = stdin.readline().strip()
    print(find(arr, N))


main()
