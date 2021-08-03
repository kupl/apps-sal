from collections import Counter
N = int(input())
s = input()
c = Counter(s)
w, r = 0, c['R']
ans = max(w, r)
for i in range(N):
    if s[i] == 'W':
        w += 1
    else:
        r -= 1
    ans = min(ans, max(w, r))

print(ans)
