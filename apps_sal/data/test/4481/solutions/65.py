n = int(input())
S = dict()
for i in range(n):
    s = input()
    if s in S:
        S[s] += 1
    else:
        S[s] = 1
ans = []
cnt = 0
for k, v in S.items():
    if v >= cnt:
        if v > cnt:
            ans = []
        ans.append(k)
        cnt = v
print(*sorted(ans), sep='\n')
