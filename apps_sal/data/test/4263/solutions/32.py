S = input()
acgt = ['A', 'C', 'G', 'T']
(ans, cnt) = (0, 0)
for i in range(len(S)):
    if S[i] in acgt:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(max(ans, cnt))
