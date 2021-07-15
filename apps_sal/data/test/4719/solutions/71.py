from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(lambda: 50+1)

for i in range(N):
    for c in range(ord("a"), ord("z")+1):
        d[chr(c)] = min(d[chr(c)], S[i].count(chr(c)))

ans = ""
for key, value in d.items():
    ans += key * value

print(ans)
