from math import factorial
n = int(input())
s = [input() for i in range(n)]
d = {}
for i in s:
    x = "".join(sorted(list(i)))
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1
ans = 0
for i in d:
    if d[i] >= 2:
        ans += factorial(d[i]) // (factorial(d[i]-2)*2)
print(ans)
