N = int(input())
A = list(map(int, input().split()))
s = [0] * (N + 1)
for i in range(N):
    s[A[i]] += 1


def nC2(n):
    return n * (n - 1) // 2


ss = list(map(nC2, s))
sss = sum(ss)
for i in range(N):
    print(sss - s[A[i]] + 1)
