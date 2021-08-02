def main():
    def z_algo(S):
        n, i, j = len(S), 1, 0
        a = [0] * n
        a[0] = n
        while i < n:
            while i + j < n and S[i + j] == S[j]:
                j += 1
            if not j:
                i += 1
                continue
            a[i], k = j, 1
            while a[k] < j - k and i + k < n:
                a[i + k] = a[k]
                k += 1
            i += k
            j -= k
        return a

    n = int(input())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    a1 = [a[i - 1] ^ a[i] for i in range(n)]
    z = z_algo([b[i - 1] ^ b[i] for i in range(n)] + a1 + a1)
    memo = []
    for i in range(n):
        if z[n + i] >= n:
            memo.append(i)
    b0 = b[0]
    for i in memo:
        print(i, b0 ^ a[i])


main()
