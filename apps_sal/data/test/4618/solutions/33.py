S = input()
K = int(input())
S_len = len(S)
ans = set()
for i in range(0, K+1):
    for j in range(0, S_len):
        if j + i <= S_len:
            t = S[j:j + i]
            if t != '':
                ans.add(t)
ans = list(ans)
ans.sort()
print((ans[K-1]))

