s = input()
K = int(input())

S = set([])
for i in range(len(s)):
    for j in range(i + 1, i + 1 + K):
        S.add(s[i:j])
ans = sorted(S)[K - 1]
print(ans)
