n = int(input())
s = map(int, input().split())
s = list(reversed(sorted(s)))
i = 1
k = []
while i < n:
    if s[i - 1] - s[i] == 1:
        k.append(s[i])
        i += 1
    elif s[i - 1] == s[i]:
        k.append(s[i])
        i += 1
    i += 1
ans = 0
for i in range(1, len(k), 2):
    ans += k[i] * k[i - 1]
print(ans)
