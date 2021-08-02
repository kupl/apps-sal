m = len(bin(n := int(input()))) - 4
A = sorted([*map(int, input().split())])[::-1]
print(2 * sum(A[:(x := 2**m - (-n + 2**-~m) // 2)]) - A[0] - n % 2 * A[x - 1])
