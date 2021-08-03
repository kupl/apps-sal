n = int(input())
s = input()
ans = 0
ans = s.count('R') * s.count('G') * s.count('B')
for i in range(n - 2):
    for d in range(1, n):
        j = i + d
        k = j + d
        if k >= n:
            break
        else:
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
print(ans)
