from collections import Counter

N = int(input())
s = [input() for _ in range(N)]

for i in range(N):
    s[i] = ''.join(sorted(s[i]))

s = Counter(s).most_common()
ans = 0
for p in s:
    ans += p[1] * (p[1] - 1) // 2

print(ans)
