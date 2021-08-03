S = input()
ans = 0
acgt = ['A', 'C', 'G', 'T']
for i in range(len(S)):
    if S[i] in acgt:
        cnt = 0
        j = i
        while j < len(S) and S[j] in acgt:
            cnt += 1
            j += 1
        ans = max(ans, cnt)

print(ans)
