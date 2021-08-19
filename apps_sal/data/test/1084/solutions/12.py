(n, m) = map(int, input().split())
t = [0] * n
for j in range(n):
    s = input()
    for i in range(len(s)):
        t[j] += int(s[i] == '#')
        t[j] *= 2
ans = True
for i in range(n):
    for j in range(i + 1, n):
        if t[i] & t[j] != 0:
            if t[i] != t[j]:
                ans = False
if ans:
    print('Yes')
else:
    print('No')
