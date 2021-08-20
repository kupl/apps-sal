n = int(input())
s = '*' + input()
r = s.count('R')
g = s.count('G')
b = s.count('B')
cnt = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        k = 2 * j - i
        if k > n:
            continue
        if s[i] != s[j] and s[j] != s[k] and (s[k] != s[i]):
            cnt += 1
print(r * g * b - cnt)
