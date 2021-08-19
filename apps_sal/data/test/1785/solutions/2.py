(n, s) = (input(), input())
a = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
A = [0, 0, 0, 0]
for x in s:
    A[a[x]] += 1
MOD = 10 ** 9 + 7
print(A.count(max(A)) ** len(s) % MOD)
