s = input()
k = int(input())
ans = []

for i in range(len(s)):
    for j in range(i + 1, min(k + i + 1, len(s) + 1)):
        ans.append(s[i:j])

ans = list(set(ans))
ans.sort()
print((ans[k - 1]))
