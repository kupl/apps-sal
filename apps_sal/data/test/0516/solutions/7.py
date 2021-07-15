n, m = map(int, input().split())
s = input()
t = input()
res = 10 ** 9
ans = []
for i in range(len(t) - len(s) + 1):
    curr = []
    for j in range(i, i + len(s)):
        if s[j - i] != t[j]:
            curr.append(j - i + 1)
    if len(curr) < res:
        res = len(curr)
        ans = curr[:]
print(res)
print(' '.join(map(str, ans)))
