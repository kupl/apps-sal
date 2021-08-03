import math


n, r = list(map(int, input().split()))
a = list(map(int, input().split()))


new = [r for i in range(n)]

for i in range(1, n):
    for j in range(i):
        temp = (2 * r)**2 - (a[i] - a[j])**2
        if(temp >= 0):
            new[i] = max(new[i], math.sqrt(temp) + new[j])
print(*new)
