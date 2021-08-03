l, k = map(int, input().split())
s = input()
c = [None] * 26
for i in range(26):
    c[i] = []
a = 1
for i in range(1, l):
    if s[i] != s[i - 1]:
        c[ord(s[i - 1]) - ord('a')].append(a)
        a = 1
    else:
        a += 1
c[ord(s[l - 1]) - ord('a')].append(a)
ans = 0
for i in range(26):
    cumm = 0
    for j in c[i]:
        cumm += j // k
    ans = max(ans, cumm)
print(ans)
