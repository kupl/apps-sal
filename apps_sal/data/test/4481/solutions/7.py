n = int(input())
S = {}
for i in range(n):
    s = input()
    if s not in S.keys():
        S[s] = 1
    else:
        S[s] += 1
m = max(S.values())
ans = []

for key, value in S.items():
    if value == m:
        ans.append(key)
ans.sort()
print(*ans, sep="\n")
