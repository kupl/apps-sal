s = input().strip()
m = input().strip()
c1 = [0] * 26
c2 = [0] * 26
for i in s:
    c1[ord(i) - ord('a')] += 1
for i in m:
    c2[ord(i) - ord('a')] += 1
ans = 0
for i in range(26):
    if c1[i] == 0 and c2[i] != 0:
        print(-1)
        return
    ans += min(c1[i], c2[i])
print(ans)
