N = int(input())
S = list(map(int, input().split()))
S = sorted(S)
a = S[0]
for i in range(N - 1):
    a = (a + S[i + 1]) / 2
print(a)
