from collections import Counter
N = int(input())
s = [input() for _ in range(N)]

# N=10^5より、O(N)で解く
for i in range(N):
    s[i] = sorted(s[i])
    s[i] = ''.join(s[i])

s = Counter(s).most_common()
ans = 0
for t in s:
    ans += t[1] * (t[1] - 1) // 2

print(ans)
