N = int(input())
S = input()
judge = [1] * N
for i in range(1, N):
    if S[i - 1] == S[i]:
        judge[i] = 0
print(sum(judge))
