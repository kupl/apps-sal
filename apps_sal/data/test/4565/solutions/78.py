n = int(input())
s = input()
(l, r) = ([], [])
ans = min(s.count('W'), s.count('E'))
k = s.count('E')
for i in range(n):
    if s[i] == 'W':
        k += 1
    else:
        k -= 1
    ans = min(ans, k)
print(ans)
