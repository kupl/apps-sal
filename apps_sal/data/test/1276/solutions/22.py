n = int(input())
s = input()

ans = s.count('R') * s.count('G') * s.count('B')

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        k = 2 * j - i
        if k < n:
            if s[k] != s[i] and s[k] != s[j] and s[i] != s[j]:
                ans -= 1
        else:
            break
print(ans)
