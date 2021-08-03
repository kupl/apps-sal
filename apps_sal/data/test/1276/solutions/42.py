n = int(input())
s = input()

r = s.count('R')
g = s.count('G')
b = s.count('B')
ans = r * g * b

for i in range(n):
    for d in range(n):
        j = i + d
        k = j + d
        if k >= n:
            break
        if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            ans -= 1

print(ans)
