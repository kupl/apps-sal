import itertools
N, K = list(map(int, input().split()))
S = input()
##num = [i for i in range(1,N + 1)]
# for i in itertools.combinations(num, 2):
# print(i)
ans = 0
for i in range(1, N):
    if S[i] == S[i - 1]:
        ans += 1

print((min(N - 1, ans + K * 2)))
