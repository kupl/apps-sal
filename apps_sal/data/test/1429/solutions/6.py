from collections import defaultdict
N, S = input().split()
N = int(N)

cnt = defaultdict(int)
answer = 0
for i in range(N):
    for s in "AGCT":
        cnt[s] = 0
    for j in range(i + 1, N, 2):
        cnt[S[j - 1]] += 1
        cnt[S[j]] += 1
        if cnt["A"] == cnt["T"] and cnt["C"] == cnt["G"]: answer += 1
        # print(cnt)

print(answer)
