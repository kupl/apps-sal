n = int(input())
s = input()
t = input()
if s.count('1') != t.count('1'):
    print(-1)
    return

p = []
ans = [0, 0]
for i in range(n):
    if s[i] != t[i]:
        if p and s[i] != p[-1]:
            p.pop(-1)
        else:
            p.append(s[i])
            w = int(s[i])
            ans[w] = max(ans[w], len(p))
print(sum(ans))
