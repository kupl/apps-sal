N, K = list(map(int, input().split()))
S = str(input())

count = 0
for i in range(N - 1):
    if S[i] != S[i + 1]:
        count += 1

print(min(N - 1, N - 1 - count + K * 2))
