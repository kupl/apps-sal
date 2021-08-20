"""
Spyder Editor

This is a temporary script file.
"""
n = int(input())
a = []
i = 1
while i * i <= n:
    if n % i == 0:
        a.append(i)
        a.append(n // i)
    i += 1
a.sort(reverse=True)
temp = 2 * n + n * n
minus = n
l = []
l.append(0)
for i in a:
    ans = (temp // i - minus) // 2
    if l[-1] != ans:
        l.append(ans)
for i in l:
    if i > 0:
        print(i, end=' ')
