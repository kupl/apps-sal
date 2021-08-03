N, K = map(int, input().split())
S = input()
num = 1
for i in range(0, len(S) - 1):
    if S[i] != S[i + 1]:
        num += 1
num = max(1, num - K * 2)
print(N - num)
