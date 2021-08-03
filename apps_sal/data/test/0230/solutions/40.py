N = int(input())
S = input()

long = 0
for i in range(N - 1):
    for j in range(i + long + 1, N):
        if not (S[i:j] in S[j:]):
            break
    long = max(long, j - i - 1)
print(long)
