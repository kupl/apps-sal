from collections import Counter
n = int(input())
x = list(map(int, input().split()))
a = []
b = []
for i in range(n):
    a.append(i+1+x[i])
    b.append(i+1-x[i])
ans = 0
a, b = Counter(a), Counter(b)
for i in range(min(a), max(b)+1):
    ans += a[i]*b[i]
print(ans)
