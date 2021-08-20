from sys import stdin, stdout


def main():
    (n, m) = list(map(int, stdin.readline().split()))
    A = [0 for _ in range(n)]
    B = [0 for _ in range(n)]
    for i in range(n):
        (A[i], B[i]) = list(map(int, stdin.readline().split()))
    tot = sum(A)
    C = [A[i] - B[i] for i in range(n)]
    C.sort()
    i = 0
    while i < n and tot > m:
        i += 1
        tot -= C[-i]
    if tot <= m:
        stdout.write('{}'.format(i))
    else:
        stdout.write('-1')


main()
