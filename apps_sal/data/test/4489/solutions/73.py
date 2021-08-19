n = int(input())
ans = 0
count = 0
s = {}
t = {}
for i in range(n):
    a = input()
    if a not in s:
        s[a] = 1
    else:
        s[a] += 1
m = int(input())
for i in range(m):
    a = input()
    if a not in t:
        t[a] = 1
    else:
        t[a] += 1
S = list(s.keys())
T = list(t.keys())
for i in range(len(S)):
    if S[i] in T:
        count = s[S[i]] - t[S[i]]
    else:
        count = s[S[i]]
    ans = max(ans, count)
print(ans)
