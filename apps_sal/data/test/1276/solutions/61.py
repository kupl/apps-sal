n = int(input())
s = input()

r = s.count('R')
g = s.count('G')
b = s.count('B')

res = r * g * b

for i in range(n):
    for j in range(n):
        jj = i + j
        k = jj + j
        if k >= n:
            break
        if s[i] != s[jj] and s[jj] != s[k] and s[k] != s[i]:
            res -= 1

print(res)
