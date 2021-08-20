S = input()
N = len(S)
K = int(input())
S_list = sorted(set(list(S)))
memo = {}
for small_char in S_list:
    for i in range(N):
        if S[i] == small_char:
            for j in range(i + 1, i + K + 1):
                word = S[i:j]
                memo[word] = None
    if len(memo) >= K:
        break
ans_list = sorted(list(memo.keys()))
print(ans_list[K - 1])
