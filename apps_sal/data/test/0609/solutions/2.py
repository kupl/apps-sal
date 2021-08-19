n = int(input())
s = input()
ans = 'YES'
s1 = s[0]
s2 = s[1]
if s[n - 1] != s1 or s1 == s2:
    ans = 'NO'
for i in range(1, n - 1):
    if s[i] != s2:
        ans = 'NO'
for i in range(1, n):
    s = input()
    p1 = i
    p2 = n - 1 - i
    if s[p1] != s1 or s[p2] != s1:
        ans = 'NO'
    for j in range(n):
        if j != p1 and j != p2 and (s[j] != s2):
            ans = 'NO'
print(ans)
