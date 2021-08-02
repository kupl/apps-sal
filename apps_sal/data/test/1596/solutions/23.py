import math

fibo = [1, 1, 2]
M = 10 ** 9 + 7
for i in range(3, 100001):
    fibo += [(fibo[i - 1] + fibo[i - 2]) % M]

s = list(input())
check = [True] * len(s)

cnt = 1
for i in range(len(s)):
    if s[i] == 'u' and check[i]:
        t = 0
        j = i
        while j < len(s) and s[j] == 'u':
            check[j] = False
            t += 1
            j += 1
        cnt = (cnt * fibo[t]) % M
    if s[i] == 'n' and check[i]:
        t = 0
        j = i
        while j < len(s) and s[j] == 'n':
            check[j] = False
            t += 1
            j += 1
        cnt = (cnt * fibo[t]) % M
    if s[i] == 'm' or s[i] == 'w':
        cnt = 0
        break

print(cnt)
